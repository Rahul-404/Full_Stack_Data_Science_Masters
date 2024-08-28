# purpose: Also deletes a file from the file system

import os

file_path = "new_file.txt"

try:
    os.unlink(file_path)
    print(f"File '{file_path}' has bee removed.")
except FileNotFoundError:
    print(f"File '{file_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to delete '{file_path}")