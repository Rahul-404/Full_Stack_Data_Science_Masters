# Aim : lists all entries in a specified directory. 
# It returns a list of the names of the entries in the directory.

# library to use functionality
import os

# Define the directory to list
directory_to_list = '.'

# List all entries in the directory
entries = os.listdir(directory_to_list)
print(f"Contents of the directory '{directory_to_list}':")
for entry in entries:
    print(entry)


