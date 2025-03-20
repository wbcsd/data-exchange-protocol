import yaml
import json
import jsonref
import logging

    
def get_property_type_spec(property):
    """
    Generates a textual representation of a JSON schema property type.
    Args:
        property (dict): A dictionary representing the JSON schema property.
    Returns:
        str: A string describing the type of the property, including additional
             information such as format, enum values, and deprecation status.
    The function handles the following property types:
    - object: Assumes the object is a reference to another type and uses its title.
    - array: Recursively processes the items in the array.
    - primitive types: Uses the type directly.
    Additional property attributes handled:
    - format: Appends the format to the type description.
    - enum: Indicates that the property is an enumeration and lists the possible values.
    - obsolete: Marks the property as obsolete.
    - deprecated: Marks the property as deprecated.
    - const: Indicates that the property has a constant value.
    """
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
        text += "<div class='json-schema-enum'>\n"
        for enum in property["enum"]:
            text += f"`\"{enum}\"` "
        text += "\n</div>"

    return text


def get_example_text(name, property):
    """
    Generates a formatted JSON example text for a given property.
    Args:
        name (str): The name of the property.
        property (dict): The property dictionary which may contain an "examples" key.
    Returns:
        str: A formatted string containing the JSON example wrapped in a code block.
    """
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

def write_defs_start(output, namespace=None, headers=['Name', 'Description']):
    if namespace:
        output.write(f"<table class='data' dfn-for='{namespace}' dfn-type='element-attr'>\n")
    else:
        output.write("<table class='data'>\n")
    if headers:
        output.write("<thead>\n")
        output.write("<tr>\n")
        for header in headers:
            output.write(f"<th>{header}</th>\n")
        output.write("</tr>\n")
        output.write("</thead>\n")
    output.write("<tbody>\n")

def write_defs_end(output):
    output.write("</table>\n\n")


def write_property(output, type, name, property, termdef=True, recursive=False):
    """
    Writes an HTML table row representing a property in a JSON schema.

    Args:
        output (io.TextIOWrapper): The output stream to write the HTML to.
        type (dict): The JSON schema type definition containing the property.
        name (str): The name of the property.
        property (dict): The property definition from the JSON schema.

    Returns:
        None
    """
    output.write("<tr>\n")
    if termdef:
        output.write(f"<td><dfn>{name}</dfn></td>\n")
    else:
        output.write(f"<td>`{name}`</td>\n")
    output.write("<td>\n")
    output.write("<div class='json-schema-type'>")
    if 'required' in type and name in type['required']:
        output.write("<span class='json-schema-required'>required</span> ")
    output.write(get_property_type_spec(property) + "</div>\n")
    output.write("\n\n")
    output.write(property["description"].strip().replace("\n\n\n", "\n\n\n\n"))
    output.write(get_example_text(name, property))
    output.write("\n")
    if property.get("x-unit"):
        output.write(f"\n<div class='json-schema-unit'>{property['x-unit']}")
        if property.get("comment"):
            output.write(f"<br>\n{sanitize(property['comment'])}")
        output.write("</div>\n")
    output.write("</td></tr>\n")
    if recursive and property["type"] == "object" and "properties" in property and not "title" in property:
        for sub_name, sub_property in property["properties"].items():
            write_property(output, property, name + "." + sub_name, sub_property, termdef)



def write_parameter(output, name, parameter):
    """
    Writes an HTML table row representing a parameter in a JSON schema.

    Args:
        output (io.TextIOWrapper): The output stream to write the HTML to.
        type (dict): The JSON schema type definition containing the parameter.
        name (str): The name of the parameter.
        parameter (dict): The parameter definition from the JSON schema.

    Returns:
        None
    """
    output.write("<tr>\n")
    output.write(f"<td><dfn>{name}</dfn> ({parameter['in']})</td>\n")
    output.write("<td>\n")
    output.write("<div class='json-schema-type'>")
    if 'required' in parameter and parameter['required'] == True:
        output.write("<span class='json-schema-required'>required</span> ")
    output.write(get_property_type_spec(parameter['schema']) + "</div>\n")
    output.write("\n\n")
    output.write(parameter["description"].strip().replace("\n\n\n", "\n\n\n\n"))
    output.write(get_example_text(name, parameter))
    output.write("\n")
    output.write("</td></tr>\n")



def sanitize(text):
    return text.replace("<", "&lt;").replace(">", "&gt;")


def generate_type_description(output, schema, type_name, type):
    """
    Generates a markdown description for a given type schema and writes it to the provided output.
    Args:
        schema (dict): The entire schema containing the type definitions.
        type_name (str): The name of the type being described.
        type (dict): The type definition containing properties, descriptions, examples, etc.
        output (TextIO): The output stream to write the markdown description to.
    Writes:
        A markdown formatted description of the type to the output stream, including sections for:
        - Title
        - Description
        - Example
        - Properties
        - External Docs
        - Examples
    """
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
        output.write("\n</div>\n\n")
    if "properties" in type:
        output.write("### Properties\n\n")
        write_defs_start(output, title)
        for name, property in type["properties"].items():
            if property.get("obsolete"):
                continue
            write_property(output, type, name, property)
        write_defs_end(output)
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
     

def generate_data_model(input_path, output_path):
    # Load the schema from the file
    with open(input_path, encoding="utf-8") as input:
        schema_unresolved = yaml.safe_load(input)
    schema = jsonref.replace_refs(schema_unresolved, merge_props=True)

    # Generate the data model in Bikeshed format
    with open(output_path, "w", encoding="utf-8") as output:
        for name,type in schema["components"]["schemas"].items():
            # Skip all types that are only used for requests or responses
            if name.endswith("Event") or name.endswith("Request") or name.endswith("Response"):
                continue
            # Skip all types without a title
            if not "title" in type:
                continue
            logging.debug(name)
            # for name in ["ProductFootprint", "CarbonFootprint"]:
            generate_type_description(output, schema, name, type)


def generate_operation(output, path, method, operation):
    output.write(f"## <dfn>{operation['summary']}</dfn>")
    output.write("\n")
    query = "?params=value&..." if "parameters" in operation and any(p["in"] == "query" for p in operation["parameters"]) else ""
    output.write(f"```HTTP\n{method.upper()} {path}{query}\n```\n")
    output.write(f"{operation['description']}\n\n")
    logging.debug(operation['description'])
    if operation.get("parameters"):
        output.write("### Parameters\n")
        write_defs_start(output)
        for param in operation["parameters"]:
            #file.write(f"- **{param['name']}** ({param['in']}): {param['description']}\n")
            # output.write(f"<tr>\n  <td><dfn>{param['name']}</dfn> ({param['in']})\n")
            # output.write(f"  <td>{param['description']}\n")
            write_parameter(output, param['name'], param)
        write_defs_end(output)

    if  operation.get("requestBody"):
        for content_type, content in operation["requestBody"]["content"].items():
            if "oneOf" in content["schema"]:
                for variant in content["schema"]["oneOf"]:
                    output.write(f"### {variant['title']}\n\n")
                    output.write(variant["description"])
                    output.write("\n\n**Request Body**\n\n")
                    output.write(f"`content-type: {content_type}`\n")
                    write_defs_start(output)
                    for name, property in variant["properties"].items():
                        write_property(output, variant, name, property, termdef=False, recursive=True)
                    write_defs_end(output)
                    if "examples" in variant:
                        output.write(variant['examples'][0])
            else:
                output.write("\n\n**Request Body**\n\n")
                output.write(f"`content-type: {content_type}`\n")
                write_defs_start(output)
                for name, property in content["schema"]["properties"].items():
                    write_property(output, variant, name, property, termdef=False)
                write_defs_end(output)


    output.write("\n")
    output.write("### Responses\n")
    output.write("`content-type: application/json`\n") 
    write_defs_start(output, headers=['Status', 'Response'])
    for status, response in operation["responses"].items():
        output.write(f"<tr>\n")
        output.write(f"<td>**{status}**</td>\n")
        output.write(f"<td>{response['description']}\n\n")
        if not "content" in response:
            output.write("No content\n")
        elif status >= "200" and status < "300":
            for content_type, content in response["content"].items():
                write_defs_start(output, headers=None)
                for name, property in content["schema"]["properties"].items():
                    logging.debug(name)
                    write_property(output, content['schema'], name, property, termdef=False)
                write_defs_end(output)
        output.write("</td>\n</tr>\n")
    write_defs_end(output)
    output.write("\n")


def generate_rest_api(input_path, output_path):
    # Load the schema from the file
    with open(input_path, encoding="utf-8") as input:
        schema_unresolved = yaml.safe_load(input)
    schema = jsonref.replace_refs(schema_unresolved, merge_props=True)

    # Generate the REST API in Bikeshed format
    with open(output_path, "w", encoding="utf-8") as output:

        for path, path_item in schema["paths"].items():
            for method, operation in path_item.items():
                generate_operation(output, path, method, operation)




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
