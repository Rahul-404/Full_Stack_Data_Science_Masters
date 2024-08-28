# Aim : check if path exists

# library to use functionality
import os

# Define a path to check
path_to_check = 'folder/subfolder/file.txt'

# Check if the path exists
if os.path.exists(path_to_check):
    print(f"The path '{path_to_check}' exists.")
else:
    print(f"The path '{path_to_check}' does not exist.")
