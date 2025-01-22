#!/bin/bash

# Check if all three parameters are provided
if [ $# -ne 3 ]; then
    echo "Error: Please provide all required parameters"
    echo "Usage: $0 <directory_path> <filename> <keyword>"
    exit 1
fi

# Store parameters in variables
directory_path="$1"
filename="$2"
keyword="$3"
full_path="$directory_path/$filename"

# Create a temporary file
temp_file=$(mktemp)

# Read the file and exclude lines containing the keyword
grep -v "$keyword" "$full_path" > "$temp_file"

# Replace the original file with the modified content
mv "$temp_file" "$full_path"

echo "Successfully removed lines containing '$keyword' from '$filename'"