# Aim : creates a directory and any intermediate directories that do not exist. 
# It is useful for creating nested directories in a single call. 
# The exist_ok parameter can be set to True to avoid raising an error 
# if the target directory already exists.

# library to use functionality
import os

# Define the path of nested directories to create
nested_directories = 'parent_directory/child_directory/grandchild_directory'

# Create the directories
os.makedirs(nested_directories, exist_ok=True)
print(f"Directories '{nested_directories}' created successfully.")
