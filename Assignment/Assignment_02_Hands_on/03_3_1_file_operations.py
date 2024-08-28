# Aim: deletes a file at the specified path. 
# It will raise an error if the file does not exist or if it is not a file (e.g., it's a directory)

import os

# Define the file to remove
file_to_remove = 'file_to_delete.txt'

# Create the file to remove (for demonstration)
with open(file_to_remove, 'w') as file:
    file.write('This file will be deleted.')

# Remove the file
if os.path.exists(file_to_remove):
    os.remove(file_to_remove)
    print(f"File '{file_to_remove}' removed successfully.")
else:
    print(f"File '{file_to_remove}' does not exist.")
