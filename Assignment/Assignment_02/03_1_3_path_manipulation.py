# Aim : to convert relative path  to absolute path

# library to use functionality
import os

# Define a relative path
relative_path = 'folder/subfolder/file.txt'

# Get the absolute path
absolute_path = os.path.abspath(relative_path)

print(f"Absolute path: {absolute_path}")
