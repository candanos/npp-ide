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


from path import Path

# path is a little better than pathlib. Path obj is also a string type.