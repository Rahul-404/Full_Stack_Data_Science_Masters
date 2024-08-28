# Aim : creates a single directory at the specified path. 
# It does not create intermediate directories if they don't already exist

# library to use functionality
import os

# directory path
directory = "new_directory"

# creating directory
if not os.path.exists(directory):
    os.mkdir(directory)
    print(f"Directory '{directory}' created successfully.")
else:
    print(f"Directory '{directory}' already exists.")