import os
import sys
import yaml
import json
import jsonref
import markdown

    
def generate_type_description(schema, type, output):
    if "description" in type:
        output.write(f"## {type['title']}\n")
        description = type["description"].strip()
        print(description)
        description = description.replace("\n\n", "\n\n\n")
        print(description)
        output.write(f"{description}\n")
        output.write("\n")
    if "properties" in type:
        output.write("### Properties\n")
        output.write("\n")
        output.write("<table class='data'>\n")
        output.write("<thead>\n")
        output.write("<tr>\n")
        output.write("  <th>Name</th>\n")
#        output.write("  <th nowrap='nowrap'>Type</th>\n")
        output.write("  <th>Description</th>\n")
        output.write("<tbody>\n")
        for name, property in type["properties"].items():
            output.write("<tr>\n")
            output.write(f"  <td>{name}\n")

            text = property["type"].strip()

            if "format" in property:
                text += f" &lt;{property['format']}&gt;"
            if "enum" in property:
                text += " &lt;enum&gt;<br/>"
                for enum in property["enum"]:
                    text += f" `\"{enum}\"`"
            output.write("  <td>" + text + "\n\n")

            text = property["description"].strip().replace("\n\n\n", "\n\n\n\n")

            if "example" in property:
                text += "\n\n"
                text += f"    {property['example']}\n"
            if "examples" in property:
                text += "\n\n```json\n"
                for example in property["examples"]:
                    text += f"{example}\n"
                text += "```\n"

            #output.write(f"  <td nowrap>{type_desc}\n")
            output.write(f"{text}\n")
        output.write("</table>\n\n")
    if "allOf" in type:
        output.write("### All Of\n")
        output.write("\n")
        for sub_type in type["allOf"]:
            generate_type_description(schema, sub_type, output)
    if "oneOf" in type:
        output.write("### One Of\n")
        output.write("\n")
        for sub_type in type["oneOf"]:
            generate_type_description(schema, sub_type, output)
    if "anyOf" in type:
        output.write("### Any Of\n")
        output.write("\n")
        for sub_type in type["anyOf"]:
            generate_type_description(schema, sub_type, output)
    if "enum" in type:
        output.write("### Enum\n")
        output.write("\n")
        for value in type["enum"]:
            output.write(f"* {value}\n")
        output.write("\n")
    if "example" in type:
        output.write("### Example\n")
        output.write("\n")
        output.write(f"```json\n{json.dumps(type['example'], indent=2)}\n```\n")
        output.write("\n")
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

    # TODO: validate schema
    
    # Open text file for writing in unicode
    with open(f"{output}.generated.md", "w", encoding="utf-8") as file:

        # Generate the data model
        for name in ["ProductFootprint", "CarbonFootprint"]:
                generate_type_description(schema, schema["components"]["schemas"][name], file)
