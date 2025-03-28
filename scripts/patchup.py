#!/usr/bin/env python3
import datetime
import sys
import re

# This script is used to patch the output html file generated by Bikeshed and
# add the status and version to the title of the html file.
#
# It takes 2 parameters: 
#  - the path to a bikeshed source file
#  - the (already generated) output html file 
#
# The script parses the header of the bikeshed file to determine STATUS, DATE and VERSION.
# These are included in the bikeshed source file as follows:
#
#   Text Macro: DATE 20241021
#   Text Macro: VERSION 2.3.0
#   Text Macro: STATUS LD|Draft|Release
#

# Parse the bikeshed file to extract the title, date, version and status.
def parse_bikeshed_file(bikeshed_file):
    with open(bikeshed_file, 'r') as file:
        content = file.read()
    match = re.search(r'Title:\s+(.*)\n', content)
    title = match.group(1) if match else None

    match = re.search(r'Text Macro: DATE\s+(\d+)', content)
    date = match.group(1) if match else None
    
    match = re.search(r'Text Macro: VERSION\s+([\d.]+)', content)
    version = match.group(1) if match else None
    
    match = re.search(r'Text Macro: STATUS\s+(\w+)', content)
    status = match.group(1) if match else None
    
    return title, date, version, status

INCLUDE_HEADER = """
<link href="../assets/markdown.css" rel="stylesheet" />
<link href="../assets/custom.css" rel="stylesheet" />
"""

# Patch the already generated html file with adapted title and status.
def update_html_file(html_file, title, status):
    with open(html_file, 'r') as file:
        content = file.read()  
    content = re.sub(r'(<title>).*(</title>)', r'\1' + title + r'\2', content, count=1)
    content = re.sub(r'(<h1 .*>).*(</h1>)', r'\1' + title + r'\2', content, count=1)
    subtitle = status
    if status == "LD":
        subtitle = "Living Document" 
    content = re.sub(r'(<h2 .* id="profile-and-date">).*(</h2>)', r'\1' + subtitle + r'\2', content, count=1)
    # Patch some CSS as well. 
    content = re.sub(r'^\s*<body', INCLUDE_HEADER + '<body', content, count=1, flags=re.MULTILINE)
    with open(html_file, 'w') as file:
        file.write(content)

# Patch the spec
def patchup(input, output):
    title, date, version, status = parse_bikeshed_file(input)
    if title is None:
        raise "Title not found"
    
    today = datetime.datetime.now().strftime('%Y%m%d')
    if status == "Release":
        title += f" (Version {version})"
    elif status in ["LD"]:
        # override with date of today
        title += f" ({version}-{today})"
    elif status in ["Draft", "Consultation"]:
        # todo: check and warn if date != today
        title += f" ({version}-{date})"
    else:
        print("Unknown status")
        return
    
    update_html_file(output, title, status)


def extract_property_descriptions(input_file_path):
    # Read the input file
    with open(input_file_path, 'r') as file:
        content = file.read()
    
    # Extract the property descriptions using regular expressions
    pattern = re.compile(r'<td><dfn>(.*?)</dfn>.*?<td>.*?<td>.*?<td>(.*?)(<tr>|</table>)', re.MULTILINE + re.DOTALL)
    matches = pattern.findall(content)
    
    # Prepare the descriptions in the required format
    descriptions = []
    for match in matches:
        property_name = match[0].strip()
        description = match[1].strip()
        descriptions.append(f"{property_name}:\n  description: |\n    {description}")
    
    return descriptions


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: patch-up-spec.py <bikeshed_file> <html_file>")
        sys.exit(1)
    
    patchup(sys.argv[1], sys.argv[2])
