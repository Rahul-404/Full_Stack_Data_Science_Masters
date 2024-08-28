try:
    # Attempt to open a file that may not exists
    with open("non-existing_file.txt", "r") as file:
        # Read the content of the file
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("Error: the file does not exists.")
except Exception as e:
    # Handle any other unexpected exceptions
    print(f"An unexpected error occured: {e}")