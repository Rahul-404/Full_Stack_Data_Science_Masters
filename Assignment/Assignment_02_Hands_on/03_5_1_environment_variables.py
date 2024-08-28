# Aim:  retrieves the value of an environment variable. 
# If the environment variable is not found, 
# it can return a default value if specified, 
# or None if no default value is provided.

import os

# Retrieve the value of the 'PATH' environment variable
path_value = os.getenv('PATH')

print(f"PATH: {path_value}")

# Retrieve the value of a non-existent environment variable with a default value
example_var = os.getenv('MY_NON_EXISTENT_VAR', 'Default Value')
print(f"MY_NON_EXISTENT_VAR: {example_var}")
