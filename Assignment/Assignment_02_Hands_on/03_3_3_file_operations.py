# Aim: retrieves the status of a file or directory. 
# It returns an os.stat_result object that contains information such as file size, 
# modification time, and permissions.

import os
import time

# Define the file to get the status
file_to_stat = 'new_file.txt'

# Create the file to stat (for demonstration)
with open(file_to_stat, 'w') as file:
    file.write('This file will be statted.')

# Get the file status
if os.path.exists(file_to_stat):
    stats = os.stat(file_to_stat)
    
    print(f"File '{file_to_stat}' status:")
    print(f"  Size: {stats.st_size} bytes")
    print(f"  Created: {time.ctime(stats.st_ctime)}")
    print(f"  Modified: {time.ctime(stats.st_mtime)}")
    print(f"  Accessed: {time.ctime(stats.st_atime)}")
    print(f"  Permissions: {oct(stats.st_mode)}")
else:
    print(f"File '{file_to_stat}' does not exist.")