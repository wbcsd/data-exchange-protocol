#!/bin/bash

# Shell script which takes 2 parameters: 
#  1) the path to a bikeshed file and
#  2) the (already generated) corresponding html file.
#
# The script parses the header of the bikeshed file to determine STATUS, DATE and VERSION.
# These are included in the bikeshed file as follows:
#   Text Macro: DATE 20230201
#   Text Macro: VERSION 1.0.1
#   Text Macro: STATUS Release
#
# If the STATUS is "Release", the following suffix will be added to the title of the html " Version ($VERSION)".
# If the STATUS is "Draft" or "Consultation" the following suffix will be added to the title of the html " (Draft $VERSION-$DATE)".
# 
# The script takes the html file and replaces the title with the new title. The title is found between <title> and </title> tags and 
# between the first <h1> and </h1> tags.
# In a similar fastion the content between the first <h2> and </h2> will be replaced with the STATUS
#  
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <path-to-bikeshed-file> <path-to-html-file>"
    exit 1
fi

bikeshed_file=$1
html_file=$2

# Extract DATE, VERSION, and STATUS from the bikeshed file
DATE=$(sed -n 's/^Text Macro: DATE //p' "$bikeshed_file")
VERSION=$(sed -n 's/^Text Macro: VERSION //p' "$bikeshed_file")
STATUS=$(sed -n 's/^Text Macro: STATUS //p' "$bikeshed_file")

echo "DATE: $DATE"
echo "VERSION: $VERSION"
echo "STATUS: $STATUS"
exit 1

# Determine the new title suffix based on STATUS
if [ "$STATUS" == "Release" ]; then
    TITLE=" Version ($VERSION)"
else
    TITLE_SUFFIX=" (Draft $VERSION-$DATE)"
fi

# Update the title in the HTML file
sed -i '' "s/<title>.*<\/title>/<title>&$TITLE_SUFFIX<\/title>/" "$html_file"
sed -i '' "s/<h1>.*<\/h1>/<h1>&$TITLE_SUFFIX<\/h1>/" "$html_file"
sed -i '' "s/<h2>.*<\/h2>/<h2>$STATUS<\/h2>/" "$html_file"