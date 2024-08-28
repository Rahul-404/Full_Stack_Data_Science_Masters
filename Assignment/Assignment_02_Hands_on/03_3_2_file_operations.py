# Aim: renames (or moves) a file or directory from src to dst. 
# This can be used to rename a file or directory, or to move it to a different location.

import os

# Define the current name and the new name
old_name = 'old_file.txt'
new_name = 'new_file.txt'

# Create the file to rename (for demonstration)
with open(old_name, 'w') as file:
    file.write('This file will be renamed.')

# Rename the file
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"File '{old_name}' renamed to '{new_name}' successfully.")
else:
    print(f"File '{old_name}' does not exist.")
