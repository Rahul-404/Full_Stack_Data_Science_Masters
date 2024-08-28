# Aim: returns the current working directory as a string. 
# This is the directory from which your script is running or where relative paths are resolved.

import os

# Get the current working directory
current_directory = os.getcwd()

print(f"Current working directory: {current_directory}")
