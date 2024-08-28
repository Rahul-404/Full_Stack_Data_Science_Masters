# Aim : join paths

# library to use functionality
import os

# Define directory and file names
directory = 'folder'
subdirectory = 'subfolder'
filename = 'file.txt'

# Join the paths
full_path = os.path.join(directory, subdirectory, filename)

print(f"Full path: {full_path}")
