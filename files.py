def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

try:
    # Ask user for the input filename
    input_filename = input("Enter the name of the file to read: ")

    # Try to open and read the file
    with open(input_filename, 'r') as infile:
        original_content = infile.read()

    # Modify the content
    modified_content = modify_content(original_content)

    # Write to a new file
    output_filename = "modified_" + input_filename
    with open(output_filename, 'w') as outfile:
        outfile.write(modified_content)

    print(f"Modified content written to '{output_filename}' successfully.")

except FileNotFoundError:
    print("❌ Error: The file does not exist. Please check the filename and try again.")
except IOError:
    print("❌ Error: Unable to read or write the file due to an I/O issue.")