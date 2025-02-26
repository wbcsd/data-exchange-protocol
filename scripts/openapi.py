import os
import sys
import yaml
import json
import jsonref
import markdown

    
def get_property_type_spec(property):
    text = ""
    if property["type"] == "object":
        # Assume that the object is a reference to another type.
        if not "title" in property:
            # raise KeyError(f"`title` denoting type name for {type_name}.{name} missing for sub-object")
            text = "object"
        else:
            text = f'<{{{property["title"]}}}>' 
    elif property["type"] == "array":
        if "items" in property:
            text  = f"array of " + get_property_type_spec(property["items"])
            # todo add minItems and maxItems
            # todo add uniqueItems
    else:
        text = property["type"].strip()

    if "format" in property:
        text += f" &lt;{property['format']}&gt;"
    if "enum" in property:
        text += " &lt;enum&gt;"
    
    if "obsolete" in property:
        text += "<span class='json-schema-obsolete'>obsolete</span>"
    if "deprecated" in property:
        text += "<span class='json-schema-obsolete'>deprecated</span>"

    if "const" in property:
        text += f" = `\"{property['const']}\"`"   

    if "enum" in property:
        text += "<div class='json-schema-enum'>"
        for enum in property["enum"]:
            text += f" `\"{enum}\"`"    
        text += "</div>"

    return text


def get_example_text(name, property):
    text = ""
    example = None
    if "examples" in property:
        example = property["examples"][0]
    if example:
        # create valid json string, with indentation. Wrap long lines if possible at 60 characters
        jsontext = ""
        for line in json.dumps(example, indent=2).splitlines():
            while len(line) > 60:
                pos = max(line.rfind(' ', 0, 60), line.rfind(',', 0, 60))
                if pos == -1:
                    pos = 60
                jsontext += line[:pos] + "\n"
                line = line[pos:].lstrip()
            jsontext += line + "\n"
        text += "\n\n```json\n"
        text += f'"{name}": {jsontext.strip()}\n'
        text += "```\n"
    
    return text

def write_property(output, type, name, property):
    output.write("<tr>\n")
    output.write(f"  <td><dfn>{name}</dfn>\n")
    output.write("  <td>\n")
    output.write("  <div class='json-schema-type'>")
    if 'required' in type and name in type['required']:
        output.write("  <span class='json-schema-required'>required</span>\n")
    output.write(get_property_type_spec(property) + "</div>\n")
    output.write("  \n\n")
    output.write(property["description"].strip().replace("\n\n\n", "\n\n\n\n"))
    output.write(get_example_text(name, property))
    output.write("\n")
    if property.get("x-unit"):
        output.write(f"<div class='json-schema-unit'>{property['x-unit']}")
        if property.get("comment"):
            output.write(f"<br>\n{sanitize(property['comment'])}")
        output.write("</div>\n")


def sanitize(text):
    return text.replace("<", "&lt;").replace(">", "&gt;")

def generate_type_description(schema, type_name, type, output):
    title = type.get("title") or type_name
    output.write(f"## <dfn element>{title}</dfn>\n")
    if "description" in type:
        description = type["description"].strip()
        description = description.replace("\n\n", "\n\n\n")
        output.write(f"{description}\n")
        output.write("\n")
    if "example" in type:
        output.write('<div class="example">\n')
        output.write(type['example'])
        output.write("\n</div>\n")
    if "properties" in type:
        output.write("### Properties\n")
        output.write("\n")
        output.write(f"<table class='data' dfn-for='{title}' dfn-type='element-attr'>\n")
        output.write("<thead>\n")
        output.write("<tr>\n")
        output.write("  <th>Name</th>\n")
        output.write("  <th>Description</th>\n")
        output.write("<tbody>\n")
        for name, property in type["properties"].items():
            if property.get("obsolete"):
                continue
            write_property(output, type, name, property)

        output.write("</table>\n\n")
    if "allOf" in type:
        output.write("### All Of\n")
        output.write("\n")
        for sub_type in type["allOf"]:
            generate_type_description(schema, name, sub_type, output)
    if "oneOf" in type:
        output.write("### One Of\n")
        output.write("\n")
        for sub_type in type["oneOf"]:
            generate_type_description(schema, name, sub_type, output)
    if "anyOf" in type:
        output.write("### Any Of\n")
        output.write("\n")
        for sub_type in type["anyOf"]:
            generate_type_description(schema, name, sub_type, output)
    if "enum" in type:
        output.write("### Enum\n")
        output.write("\n")
        for value in type["enum"]:
            output.write(f"* {value}\n")
        output.write("\n")
    # if "example" in type:
    #     output.write("### Example\n")
    #     output.write("\n")
    #     output.write(f"```json\n{json.dumps(type['example'], indent=2)}\n```\n")
    #     output.write("\n")
    if "x-externalDocs" in type:
        output.write("### External Docs\n")
        output.write("\n")
        output.write(f"[{type['x-externalDocs']['description']}]({type['x-externalDocs']['url']})\n")
        output.write("\n")
    if "x-examples" in type:
        output.write("### Examples\n")
        output.write("\n")
        for example in type["x-examples"]:
            output.write(f"#### {example['title']}\n")
            output.write("\n")
            output.write(f"{example['description']}\n")
            output.write("\n")
     
def generate_data_model(input, output):
    # Load the schema from the file
    with open(input, encoding="utf-8") as file:
        schema_unresolved = yaml.safe_load(file)
    schema = jsonref.replace_refs(schema_unresolved, merge_props=True)

    # Generate the data model in Bikeshed format
    with open(output, "w", encoding="utf-8") as file:
        for name,type in schema["components"]["schemas"].items():
            # Skip all types that are only used for requests or responses
            if name.endswith("Event") or name.endswith("Request") or name.endswith("Response"):
                continue
            # Skip all types without a title
            if not "title" in type:
                continue
            print(name)
            # for name in ["ProductFootprint", "CarbonFootprint"]:
            generate_type_description(schema, name, type, file)

def generate_operation(output, path, method, operation, variant = None):
    output.write(f"## {operation['summary']}")
    if variant:
        output.write(f": {variant['title']}")
    output.write("\n")
    output.write(f"{variant and variant.get('description') or operation['description']}\n\n")
    output.write(f"```HTTP\n{method.upper()} {path}\n```\n")
    if operation.get("parameters"):
        output.write("### Query Parameters\n")
        output.write(f"<table class='data' dfn-for='{operation['operationId']}' dfn-type='element-attr'>\n")
        output.write("<thead>\n")
        output.write("<tr>\n")
        output.write("  <th>Name</th>\n")
        output.write("  <th>Description</th>\n")
        output.write("<tbody>\n")
        for param in operation["parameters"]:
            #file.write(f"- **{param['name']}** ({param['in']}): {param['description']}\n")
            output.write(f"<tr>\n  <td>**{param['name']}** ({param['in']})\n")
            output.write(f"  <td>{param['description']}\n")
    output.write("</table>\n\n")

    if not variant:
        variant = operation.get("requestBody")
    if variant:
        output.write("### Request Body\n")
        output.write("`content-type: application/cloudevents+json`\n") 
        output.write(f"<table class='data' dfn-for='{operation['operationId']}' dfn-type='element-attr'>\n")
        output.write("<thead>\n")
        output.write("<tr>\n")
        output.write("  <th>Name</th>\n")
        output.write("  <th>Description</th>\n")
        output.write("<tbody>\n")
        for name, property in variant["properties"].items():
            write_property(output, variant, name, property)
        output.write("</table>\n\n")

    output.write("\n")
    output.write("### Responses\n")
    for status, response in operation["responses"].items():
        output.write(f"- **{status}**: {response['description']}\n")
        if response.get("content"):
            for content_type, content in response["content"].items():
                for name, property in content["schema"]["properties"].items():
                    print(name)
                    print(property)
                    write_property(output, content['schema'], name, property)
                    # output.write(f"  - **{name}**\n")
    output.write("\n")

def generate_rest_api(input, output):
    # Load the schema from the file
    with open(input, encoding="utf-8") as file:
        schema_unresolved = yaml.safe_load(file)
    schema = jsonref.replace_refs(schema_unresolved, merge_props=True)

    # Generate the REST API in Bikeshed format
    with open(output_path, "w", encoding="utf-8") as output:

        for path, path_item in schema["paths"].items():
            for method, operation in path_item.items():

                if operation.get("requestBody"):
                    if operation["requestBody"]["content"]["application/cloudevents+json"]["schema"].get("oneOf"):
                        for request_object in operation["requestBody"]["content"]["application/cloudevents+json"]["schema"]["oneOf"]:
                            generate_operation(file, path, method, operation, request_object)
                else:
                    generate_operation(file, path, method, operation)




def test(input):
    with open(input, encoding="utf-8") as file:
        schema_unresolved = yaml.safe_load(file)
    print(json.dumps(schema_unresolved["components"]["schemas"]["ProductFootprint"], indent=2))
    print(schema_unresolved["components"]["schemas"]["ProductFootprint"]["properties"]["statusComment"])
    schema = jsonref.replace_refs(schema_unresolved, merge_props=True)
    print("===================\n")
    print(schema["components"]["schemas"]["ProductFootprint"]["properties"]["pcf"])
    print(schema["components"]["schemas"]["ProductFootprint"]["properties"]["pcf"]["properties"]["pCfExcludingBiogenic"])
    #schema = jsonref.replace_refs(schema_unresolved, merge_props=True)
    #print(json.dumps(schema["components"]["schemas"]["ProductFootprint"], indent=2))
