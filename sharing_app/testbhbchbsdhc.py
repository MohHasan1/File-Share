import os

def get_filename_from_path(file_path):
    return os.path.basename(file_path)

# Example usage:
file_path = "/path/to/source/file.txt"
filename = get_filename_from_path(file_path)

print(filename)