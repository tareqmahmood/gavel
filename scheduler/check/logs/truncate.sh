#!/bin/bash

# Define the base directory containing the subdirectories with text files
base_directory="."

# Iterate over each text file found in the base directory and its subdirectories
find "$base_directory" -type f -name "*.txt" | while read -r file; do
    # Extract the last 20 lines of the file and overwrite the original file
    tail -n 20 "$file" > "$file.tmp" && mv "$file.tmp" "$file"
done