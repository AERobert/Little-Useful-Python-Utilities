#!/usr/bin/env python3

from pathlib import Path
import sys

def replace_smart_quotes(file_path):
    try:
        # Define the mappings of smart quotes to straight quotes
        replacements = {
            "\u2018": "'",  # Left single quote
            "\u2019": "'",  # Right single quote
            "\u201C": '"',  # Left double quote
            "\u201D": '"'   # Right double quote
        }

        # Read the original file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace smart quotes with straight quotes
        for smart, straight in replacements.items():
            content = content.replace(smart, straight)

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        return "Smart quotes replaced with straight quotes in " + file_path
    except FileNotFoundError:
        return "Error: File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    if len(sys.argv) != 2:
        print("Usage: smart2straight '<file_path>'")
        print("Note: Use single quotes around the file path if using wildcards.")
        sys.exit(1)

    # Use Path.glob to handle wildcard file paths
    file_paths = list(Path('.').glob(sys.argv[1]))

    # Check if any files were found
    if not file_paths:
        print("No files found.")
        sys.exit(1)

    # Apply replace_smart_quotes to each file
    for file_path in file_paths:
        result = replace_smart_quotes(file_path)
        print(result)

if __name__ == "__main__":
    main()