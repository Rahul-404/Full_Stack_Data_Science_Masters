# purpose: deletes a file from the file system

import os
import time

file_path = "example.txt"

try:
    os.remove(file_path)
    print(f"File '{file_path}' has been removed.")
except FileNotFoundError:
    print(f"File '{file_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to delete '{file_path}'.")