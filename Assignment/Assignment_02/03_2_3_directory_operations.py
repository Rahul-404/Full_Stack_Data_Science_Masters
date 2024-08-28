# Aim : removes (deletes) a single empty directory. 
# It will raise an error if the directory is not empty.

# library to use functionality
import os

# Define the directory to remove
directory_to_remove = 'new_directory'

# Remove the directory
if os.path.exists(directory_to_remove):
    os.rmdir(directory_to_remove)
    print(f"Directory '{directory_to_remove}' removed successfully.")
else:
    print(f"Directory '{directory_to_remove}' does not exist.")


