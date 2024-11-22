# ' pathlib is a solution of python after py 3.4 for handling path and filename operations.
# ' just pass a forward slashed path and it handles the rest. 
from pathlib import Path

data_folder = Path("source_data/text_files/")
file_to_open = data_folder / "raw_data.txt"

# ' and a Path instance has a lot of attributes for parsing etc. 
filename = Path("source_data/text_files/raw_data.txt")
print(filename.name)
# prints "raw_data.txt"
print(filename.suffix)
# prints "txt"
print(filename.stem)
# prints "raw_data"


# path is a little better than pathlib. Path obj is also a string type.
# but may create an additional dependency.
from path import Path



from pathlib import Path

# Example full path
file_path = "/home/user/documents/report.txt"

# Create a Path object
path = Path(file_path)

# Extract components
basename = path.name
parent_directory = path.parent
extension = path.suffix
name_without_extension = path.stem

# Print the results
print(f"Full path: {file_path}")
print(f"Basename: {basename}")
print(f"Parent directory: {parent_directory}")
print(f"Extension: {extension}")
print(f"Name without extension: {name_without_extension}")