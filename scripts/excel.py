import os
import sys
import yaml
import re
import jsonref
import logging
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment, PatternFill, Font, Border, Side
from openpyxl.drawing.spreadsheet_drawing import AnchorMarker, TwoCellAnchor, OneCellAnchor


status = " (Living Document)"


def generate_excel(ws, schema, types):
    """
    @param ws: the worksheet to write to
    @param schema: the OpenAPI schema
    @param types: list of types to include in the worksheet
    
    This function generates an Excel worksheet from an OpenAPI schema. 
    It starts with the types specified in the list and follows all
    references to other types. 
    """

    def format(item, style):
        alignment = None

        #if style.get("word_wrap"):
        #    alignment = Alignment(vertical="top", wrap_text=style.get("word_wrap"))
        #else: 
        # if style.get("vertical_align"):
        #     alignment = Alignment(vertical=style.get("vertical_align"))
        #     logging.debug(f"Setting vertical alignment to {style.get('vertical_align')}")
        #     logging.debug(alignment)

        font = Font(name=style.get("font"), size=style.get("size"), bold=style.get("bold"), color=style.get("fgcolor"), strike=style.get("strike"))

        if style.get("bgcolor"):
            fill = PatternFill(start_color=style.get("bgcolor"), end_color=style.get("bgcolor"), fill_type="solid")
        else:
            fill = None

        # Bottom border white
        border = None
        if style.get("border"):
            border = Border(bottom=Side(style="thin", color="FFFFFF"))

        if not isinstance(item, tuple):
            item = [item]
        for cell in item:
            if alignment:
                cell.alignment = alignment 
            if font:
                cell.font = font
            if fill:
                cell.fill = fill
            if border:
                cell.border = border

    # Define the columns of the worksheet
    columns = dict(
        property    = dict(title = "Attribute", width = 30),
        validation  = dict(title = "Validation", width = 15),
        description = dict(title = "User Friendly Description", width = 60, wrap_text = True, description="""
M=Mandatory
M2=Mandatory for any PCF calculated following PACT-2
M3=Mandatory for any PCF calculated following PACT-3
M2-2025=Mandatory for any PCF calculated in or after 2025 with PACT-2
M3-2027=Mandatory for any PCF calculated in or after 2027 with PACT-3""".strip()),
        unit        = dict(title = "Unit", width = 17),
        comment     = dict(title = "Comment", width = 30),
        #link       = dict(title = "Link to Methodology", width = 15),
        accepted    = dict(title = "Accepted Value(s)", width = 20, wrap_text = True),
        example1    = dict(title = "Example 1", width = 30, wrap_text = True),
        example2    = dict(title = "Example 2", width = 30, wrap_text = True),
        example3    = dict(title = "Example 3", width = 30, wrap_text = True)
    )
    i = 0
    for column in columns.values():
        column['index'] = chr(ord('A') + i)
        i += 1

    # Define a lambda function to for creating a row array of values
    row = lambda **kwargs: [kwargs[column] for column in columns.keys()]

    # Define the styles for the worksheet
    fontname           = "Aptos Narrow"
    color_title        = "08094C"
    color_table_header = "2A4879" 
    color_header       = "489F81"
    
    title_style     = dict(font = fontname, size = 16, bold = False, bgcolor = color_title, fgcolor = "FFFFFF")
    subtitle_style  = dict(font = fontname, size = 16, bold = False, bgcolor = color_title, fgcolor = "FFFFFF")
    header_style    = dict(font = fontname, bgcolor = color_table_header, fgcolor = "FFFFFF")
    heading_style   = dict(font = fontname, bold = True, bgcolor = color_header, fgcolor = "FFFFFF")
    normal_style    = dict(font = fontname) # bgcolor="EEECE2", border=True)
    bold_style      = dict(font = fontname, bold = True)
    obsolete_style  = dict(font = fontname, strike = True, fgcolor = "95261F")

    logging.info(f"Columns: {columns}")

    # Append the title and header rows
    ws.append(["PACT Simplified Tech Specs" + status, "", "", "", "", "", "", "", "", "", ""])
    ws.append([schema["info"]["version"], "", "", "", "", "", "", "", "", ""])

    # Append the column headers
    ws.append([column["title"] for column in columns.values()])
    ws.append([column.get("description","") for column in columns.values()])

    # Set cell widths
    for column in columns.values():
        ws.column_dimensions[column["index"]].width = column.get("width", 15)
    
    # format the first rows with the styles
    format(ws[1], title_style)
    format(ws[2], subtitle_style)
    format(ws[3], header_style)
    format(ws[4], header_style)

    # Inner function to get a succinct type description
    def get_type_description(info):
        type_description = ""
        if info.get("type", "") == "array":
            type_description = "array: " + get_type_description(info["items"])
        if info.get("type", "") == "object":
            if info.get("title"):
                type_description = info.get("title")
            else:
                type_description = "object"
        type_description += " " + info.get("format", "")
        if info.get("comment"):
            type_description += " (" + info["comment"] + ")\n"
        else:
            type_description += "\n"
        type_description += "|".join(info.get("enum", [])) + "\n"
        type_description = type_description.strip()
        if (type_description == ""):
            type_description = info.get("type","")
        elif not info.get("type","") in ["object","array"]:
            type_description += "\n(" + info.get("type","") + ")"
        return type_description

    # Inner function to write a property to the worksheet
    def write_property(name, info, parent, level):

        # Extract the type and description of the property
        type = info.get("type", "")
        
        if type == "object":
            write_type(name, info, level + 1)
            return
        
        type_description = get_type_description(info)
        description = info.get("summary") or info.get("description") or "N/A"
        paragraphs = description.split("\n")
        description = ""
        for paragraph in paragraphs:
            if paragraph.strip() == "":
                description += "\n\n"
            else:
                description += paragraph.strip() + " "
        description = description.strip()
        
        # experiment: change the word property to attribute, use regex for word boundary
        description = re.sub(r'\bproperty\b', 'attribute', description)

        examples = info.get("examples", []) + ['','','']
        print(examples)
        mandatory = name in parent.get("required", [])
        
        # Append a row to the worksheet
        rule = info.get("x-rule", "")
        if mandatory:
            rule = "M"
        else:
            rule = info.get("x-rule", "O")

        ws.append(row(
            property = name,
            validation = rule,
            comment = info.get("title", "") + info.get("x-comment", "") + info.get("note", ""),
            description = description,
            unit = info.get("x-unit", "-"),
            accepted = type_description,
            example1 = str(examples[0]),
            example2 = str(examples[1]),
            example3 = str(examples[2])
            ))
        # Apply styles to the row, first col (property name) will be bold
        format(ws[ws.max_row], normal_style)
        format(ws[ws.max_row][0], bold_style)
        # Strike-through obsolete or deprecated properties
        if info.get("deprecated") or info.get("obsolete"):
            format(ws[ws.max_row], obsolete_style)
        # Indent the first cell of the row just added
        ws[ws.max_row][0].alignment = Alignment(indent=level)

        if info.get("type", None) == "array" and info["items"].get("type") == "object":
            logging.debug(f"Writing array for {name} at level {level}")
            write_type(None, info["items"], level + 1)

        
    # Inner function to write a type to the worksheet
    def write_type(name, info, level=0):
        logging.debug(f"Writing type {name} at level {level}")
        if info.get("title") and name:
            # Append a row for the type itself and set background color to blue
            ws.append([name + ": " + info["title"], info.get("x-rule"), info.get("summary"), "", "", "", "", "", ""])
            format(ws[ws.max_row], heading_style)

        for prop_name, prop_info in info.get("properties", {}).items():
            # Skip obsolete properties
            if "obsolete" in prop_info:
                continue

            # Extract the type and description of the property
            logging.debug(f"Writing property {prop_name}")

            write_property(prop_name, prop_info, info, level)


    # Find the specified types in the schema
    for name in types:
        type = schema["components"]["schemas"][name]
        write_type(name, type)


    # Apply word-wrap alignment for columns description and examples
    for column in columns.values():
        for cell in ws[column["index"]]:
            cell.alignment = Alignment(
                indent = cell.alignment.indent, 
                wrap_text=column.get("wrap_text", False),
                vertical="top"
                )

    # Insert the PACT logo
    img = Image("./assets/logo-dark-margin.png")
    img.width = img.width / 5
    img.height = img.height / 5
    ws.add_image(img, "A1")
    ws.row_dimensions[1].height = img.height * 4 / 3
    ws["A1"].alignment = Alignment(vertical="bottom")


def openapi_to_excel(input_path, output_path, title, types):
    """
    @param input_path: path to the OpenAPI schema file
    @param output_path: path to the output Excel file
    @param title: title of the Excel worksheet
    @param types: list of types to include in the Excel worksheet
    """

    # Load the schema from the file
    with open(input_path) as file:
        schema = yaml.safe_load(file)
    schema = jsonref.replace_refs(schema, merge_props=True)

    # Create a new workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = title
    ws.sheet_view.zoomScale = 140

    # Generate the worksheet
    generate_excel(ws, schema, types)
    wb.save(output_path)



if __name__ == "__main__":
    # Get command line args
    if len(sys.argv) < 2:
        print("Usage: python3 generate-excel.py <input-path>")
        print("This script generates an Excel file from a OpenAPI schema.")
        print("")
        print("Example:")
        print("python3 generate-excel pact-openapi-2.2.1-wip.yaml")
        print()
        exit()
    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print("File not found:", input_path)
        exit()
    status = " (Living Document)"
    if (len(sys.argv) >= 3):
        status = " (" + sys.argv[2].upper() + ")"
    
    # Load the schema from the file
    with open(input_path) as file:
        schema1 = yaml.safe_load(file)
    schema = jsonref.replace_refs(schema1, merge_props=True)

    # Create a new workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = "PACT Simplified Data Model"
    ws.sheet_view.zoomScale = 140

    generate_excel(ws, schema, ["ProductFootprint"])

    # Save the workbook to a file
    output_path = os.path.basename(input_path)
    output_path = output_path.replace('-openapi-', '-simplified-model-')
    output_path = output_path.replace(".yaml", "") + ".xlsx"
    output_path = os.path.join(os.path.dirname(input_path), output_path)
    wb.save(output_path)
