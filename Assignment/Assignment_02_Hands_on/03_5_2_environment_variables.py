# Aim: a dictionary-like object representing the environment variables of the current process. 
# You can use it to access, modify, or delete environment variables.

import os

# Print all environment variables
print("All environment variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

# Access an environment variable using os.environ
path_value = os.environ.get('PATH')
print(f"PATH (using os.environ): {path_value}")

# Set a new environment variable
os.environ['MY_NEW_VAR'] = 'MyValue'
print(f"MY_NEW_VAR: {os.environ['MY_NEW_VAR']}")

# Delete an environment variable
del os.environ['MY_NEW_VAR']
print("MY_NEW_VAR deleted.")
