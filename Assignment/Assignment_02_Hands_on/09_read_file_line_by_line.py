import os

# create a sample file for demonstration
example_file_content = """Line 1
Line 2
Line 3
Line 4
Line 5"""

with open("example_file.txt", 'w') as file:
    file.write(example_file_content)


def read_file_line_by_line(file_path):
    """
    A generator function that yields lines from a file one by one.
    """
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip() # yield each line, stripped of training newline characters


# example usage
file_path  = "example_file.txt"

for line in read_file_line_by_line(file_path):
    print(line)

# deleting file we created for demonstration purpose
os.remove(file_path)