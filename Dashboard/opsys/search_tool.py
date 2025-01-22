from tqdm import tqdm
import os
from pathlib import Path
import re 

def list_files(directory):
    directory_path = Path(directory)
    return [file for file in directory_path.rglob('T660*') if file.is_file()]
    

def count_lines(file_path):
    """
    Efficiently count lines in a large file.
    Returns total line count and file size in MB.
    """
    try:
        line_count = 0
        file_size = os.path.getsize(file_path)
        
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            # Create progress bar based on file size
            pbar = tqdm(total=file_size, 
                      desc="Counting lines", 
                      unit="B",
                      unit_scale=True,
                      bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]')
            
            for line in file:
                line_count += 1
                pbar.update(len(line.encode('utf-8')))
            
            pbar.close()
            
            # Print summary
            print(f"\nLine count completed:")
            print(f"- Total lines: {line_count:,}")
            print(f"- File size: {file_size / (1024 * 1024):.2f} MB")
            return line_count
                
    except Exception as e:
        print(f"Error counting lines: {str(e)}")
        return 0
        
        
def get_first_line(file_path):
    """
    Efficiently get the first line of a large file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            first_line = file.readline()
            return first_line.strip()
                
    except Exception as e:
        return f"Error reading file: {str(e)}"


def get_last_line(file_path, chunk_size=1024*1024):  # 1MB chunk size
    """
    Efficiently get the last line of a large file by reading chunks from the end.
    """
    try:
        with open(file_path, 'rb') as file:
            file.seek(0, 2)  # Seek to end of file
            file_size = file.tell()
            
            if file_size == 0:
                return "Empty file"
                
            # Read last chunk first
            chunk_position = max(file_size - chunk_size, 0)
            file.seek(chunk_position)
            chunk = file.read()
            
            try:
                # Try to decode with utf-8, replace invalid characters
                last_line = chunk.decode('utf-8', errors='replace')
                
                # If we're not at file start and no newline found, read more
                while chunk_position > 0 and '\n' not in last_line:
                    chunk_position = max(chunk_position - chunk_size, 0)
                    file.seek(chunk_position)
                    chunk = file.read(min(chunk_size, file.tell()))
                    last_line = chunk.decode('utf-8', errors='replace') + last_line
                
                # Get the last line
                lines = last_line.splitlines()
                return lines[-1] if lines else ""
                
            except Exception as e:
                return f"Error decoding line: {str(e)}"
                
    except Exception as e:
        return f"Error reading file: {str(e)}"


def search_in_large_file(input_file_path, search_string, output_file_path=None):
    """
    Search for a string in a large file and save matching lines to an output file.
    Shows progress while processing.
    """
    if output_file_path is None:
        output_file_path = input_file_path.rsplit('.', 1)[0] + '_search_results.txt'
    
    # List of encodings to try
    encodings = ['utf-8', 'latin-1', 'cp1252', 'ascii']
    
    for encoding in encodings:
        try:
            # First, get the total number of lines in the file
            total_lines = sum(1 for _ in open(input_file_path, 'r', encoding=encoding, errors='replace'))
            
            # Now process the file with progress bar
            with open(input_file_path, 'r', encoding=encoding, errors='replace') as input_file, \
                 open(output_file_path, 'w', encoding='utf-8') as output_file:
                
                print(f"\nProcessing with {encoding} encoding")
                matches = 0
                
                # Create progress bar
                pbar = tqdm(total=total_lines, 
                          desc="Searching", 
                          unit="lines",
                          bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} lines [{elapsed}<{remaining}]')
                
                for line_number, line in enumerate(input_file, 1):
                    if search_string in line:
                        output_file.write(f"Line {line_number}: {line}")
                        matches += 1
                    pbar.update(1)
                
                pbar.close()
                
                # Print summary
                file_size = os.path.getsize(input_file_path) / (1024 * 1024)  # Convert to MB
                print(f"\nSearch completed:")
                print(f"- File size: {file_size:.2f} MB")
                print(f"- Total lines processed: {total_lines:,}")
                print(f"- Matches found: {matches:,}")
                print(f"- Results saved to: {output_file_path}")
                return
                
        except UnicodeError:
            print(f"Failed with {encoding} encoding, trying next...")
            continue
        except FileNotFoundError:
            print(f"Error: The file '{input_file_path}' was not found.")
            return
        except PermissionError:
            print(f"Error: Permission denied while accessing the file.")
            return
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return
    
    print("Failed to read the file with any of the attempted encodings.")


def search_in_directory_with_regex(directory, regx):   
    reportlines = []
    files = list_files(directory_to_list)
    # Get the list of all files
    print(f"{len(files)} is found in the directory!" )
    for filepath in files:
        filelines = []
        file = open(filepath, "r")
        lines = file.readlines()
        found_in = False 
        # print(f"{len(lines)} is found in the {file.name}!" )
        for i, line in enumerate(lines):
            matches = re.search(regx, line)
            if matches:
               found_in = True 
               print("found" + line) 
               filelines.append(line)
        if found_in:
            report = ''.join(filelines).rstrip()    
            reportlines.append(file.name + '\n' + report)

    for line in reportlines:
        reportfile.write(line + '\n')    
    reportfile.close()      


if __name__ == '__main__': 
    # file_path = r'C:\github\kola-log\utl_publish_log_131.txt'
    # file_path = r'C:\github\kola-log\utl_publish_log_130.txt'
    # search_term = '2024-06-11'
    # print(get_first_line(file_path)[0:50])
    # print(get_last_line(file_path)[0:50])
    # print(str(count_lines(file_path)))
    # search_in_large_file(file_path, search_term)
    directory_to_list = r'C:\github\kola-cobol\cobol' 
    reportpath = r'C:\npp-ide\Dashboard\temp\search_results.txt'
    reportfile = open(reportpath, "w+")
    rgx  = r'\bIDAVD\b\s+=\s+:\bT400-IDAVD\b' # updating a db2 field
    rgx  = r'IDAVD.*\b(IF|AND|OR)\b|\b(IF|AND|OR)\b.*IDAVD' # possible business rules for a field
    rgx  = r'\bFROM\b\s+\bITEM_MARKFOR\b' # reading a db2 table

    search_in_directory_with_regex(directory_to_list, rgx)
    
    