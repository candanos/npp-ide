from pathlib import Path

def list_files(directory):
    directory_path = Path(directory)
    return [file for file in directory_path.rglob('*') if file.is_file()]

def convert_line_endings(path):
    file = open(path, "r")
    content = file.read().replace('\r\n', '\n')
    file = open(path, "w", encoding="utf-8", newline='\n')
    file.write(content)
    file.close()

# Specify the directory you want to list files for
directory_to_list = 'C:/github/kola-cobol/cobol' 

# Get the list of all files
paths = list_files(directory_to_list)
for path in paths:
    convert_line_endings(path)