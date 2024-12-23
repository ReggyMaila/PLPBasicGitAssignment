

def read_and_write_file():
    try:
        # Ask the user for the filename to read
        input_filename = input("Enter the name of the file to read from: ")

        # Attempt to open the file for reading
        with open(input_filename, 'r') as infile:
            content = infile.readlines()  # Read all lines from the file

        # Modify the content (example: prepend line numbers)
        modified_content = [f"{i+1}: {line}" for i, line in enumerate(content)]

        # Write the modified content to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist. Please try again.")
    except PermissionError:
        print(f"Error: Permission denied for accessing the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    read_and_write_file()

