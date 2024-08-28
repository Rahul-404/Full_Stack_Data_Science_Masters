# Aim: changes the current working directory to the directory specified by path. 
# This affects how relative paths are resolved in your script.

import os

# Define the new directory path
new_directory = 'example_directory'

# Create the new directory for demonstration (if it does not exist)
if not os.path.exists(new_directory):
    os.mkdir(new_directory)

# Change the current working directory
os.chdir(new_directory)

# Verify the change
current_directory = os.getcwd()
print(f"Changed working directory to: {current_directory}")

# Optionally, change back to the original directory (if needed)
original_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(original_directory)
