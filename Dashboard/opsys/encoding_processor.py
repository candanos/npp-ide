from pathlib import Path

# Yes, if you try to read with UTF-8 encoding like:
# pythonCopywith open(filepath, "r", encoding='utf-8') as file:
# Python will throw an error when it encounters \xa4 or \xa7 by themselves because:

# In UTF-8, bytes in the range \xa0 to \xbf can only be continuation bytes (second byte of a multi-byte sequence)
# When Python sees \xa4 or \xa7 without a leading byte like \xc2, it recognizes this as invalid UTF-8
# This will cause a UnicodeDecodeError because these single bytes are not valid UTF-8 sequences

# That's why for files containing these bytes, you either need to:

# Read with Latin-1 encoding which can read any byte value, or
# Read in binary mode ("rb") and handle the byte replacements yourself before decoding

# The error you would see would look something like:
# CopyUnicodeDecodeError: 'utf-8' codec can't decode byte 0xa4 in position X: invalid start byteRetryClaude can make mistakes. Please double-check responses.


def binary_processor(binary_content):
    try:
        # Convert input text to binary
        # binary_content = text.encode('utf-8')
        # binary_content = text.encode('utf-8')
        
        # Apply the binary replacements

    # Convert the two-byte UTF-8 sequences
        # wrong mappings in mainframe. these are mapped wrong when exported from MF
        '''
        |   MF export       |   expected char   |  cp1252      | utf-8         |   
        |    b'\x5d' (])    |   tab             |  b'\x09'     | b'\x09'       |   
        |    b'\xa7' (§)    |   [               |  b'\xa7'     | b'\xc2\xa7'   |   
        |    b'\xa4' (¤)    |   ]               |  b'\xa4'     | b'\xc2\xa4'   |   
        |    b'\xd6' (Ö)    |   @               |  b'\x40'     | b'\x40'       | 
        
        '''
        # single byte utf8
        binary_content = binary_content.replace(b'\x5d', b'\t')         # Convert 5d to tab
        
        # double byte utf8
        binary_content = binary_content.replace(b'\xc2\xa7', b'[')      # Convert UTF-8 sequence for §, Convert a7 to [
        binary_content = binary_content.replace(b'\xc2\xa4', b']')      # Convert UTF-8 sequence for ¤, Convert a4 to ]
        binary_content = binary_content.replace(b'\xc2\xa6', b'\xc3\xb6') # Convert UTF-8 sequence for ¦ to ö
        # following characters are used for each other for example mf export ü instead of ~ and vice versa
        binary_content = binary_content.replace(b'\xc3\x84', b'\23')    # Ä to #   
        binary_content = binary_content.replace(b'\xc3\x96', b'\x40')   # Ö to @
        binary_content = binary_content.replace(b'\xc3\xbc', b'\x7e')   # ü to ~
        

       # binary_content = binary_content.replace(b'\xc9', b'\\')
        # binary_content = binary_content.replace(b'\xfc', b'~')          
        # binary_content = binary_content.replace(b'\xd6', b'@')          
        # binary_content = binary_content.replace(b'\xc4', b'#')          
        # binary_content = binary_content.replace(b'\xc5', b'$')          
        # binary_content = binary_content.replace(b'\xa6', b'\xc3\xb6')   
        # binary_content = binary_content.replace(b'\xa0', b'\xc2\xa0')
        # binary_content = binary_content.replace(b'\xd8', b'\xc3\x98')   
        # binary_content = binary_content.replace(b'\xd6', b'\xc3\x93')   
        # binary_content = binary_content.replace(b'\xd3', b'\xc3\x93')   
        # binary_content = binary_content.replace(b'\xb4', b'\xc2\xb4')   
        # binary_content = binary_content.replace(b'\xe8', b'\xc3\xa8')   
        # binary_content = binary_content.replace(b'\xbd', b'\xc2\xbd')   
        # binary_content = binary_content.replace(b'\xb5', b'\xc2\xb5')   
        # binary_content = binary_content.replace(b'\xea', b'\xc3\xaa')   
        

        # Convert back to text
        text_content = binary_content.decode('utf-8', errors='replace')
        
        return text_content
        
    except Exception as e:
        print(f"Error in pretty_print: {str(e)}")
        text_content = binary_content.decode('utf-8', errors='replace')
        return  text_content


def process_bad_chars(binary_linelist):
    formatted_linelist = []
    for binary_line in binary_linelist:
        text_line = binary_line.decode('utf-8', errors='replace')
        if text_line[0:3] == 'J46':
            before_dcn_body = text_line[0:15]
            dcn_body_text = binary_processor(binary_line[15:])
            text_line = before_dcn_body + dcn_body_text    
        formatted_linelist.append(text_line)       
    return formatted_linelist 


def readfile_cp1252(filepath):
    file = open(filepath, "r", encoding='cp1252', errors='replace') # replace with �
    linelist = file.read().split('\n')
    file.close()
    return linelist 


def readfile_utf8(filepath):
    file = open(filepath, "r", encoding='utf-8', errors='replace')
    linelist = file.read().split('\n')
    file.close()
    return linelist 


def readfile_binary(filepath):
    with open(filepath, "rb") as file:
        content = file.read()
        # Replace Windows-style endings with Unix-style first
        content = content.replace(b'\r\n', b'\n')
        # Replace any remaining Mac-style endings
        content = content.replace(b'\r', b'\n')
        # Now split on \n
        lines = content.split(b'\n')
        return lines


def writefile(filepath, linelist):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(line + '\n' for line in linelist)
    
    
def inspect_file_encoding(input_file):
    # First, let's look at the raw bytes
    with open(input_file, 'rb') as f:
        content = f.read()
        
    # Look at the first few bytes (useful for BOM detection)
    print("First 10 bytes:", [hex(b) for b in content[:10]])
    
    # Try to spot patterns in problematic areas
    # Let's look for bytes above 0x7F (non-ASCII bytes)
    high_bytes = [(i, hex(b)) for i, b in enumerate(content) if b > 0x7F]
    print("\nPositions and values of non-ASCII bytes:")
    for pos, byte in high_bytes[:10]:  # Show first 10 occurrences
        print(f"Position {pos}: {byte}")
        
    # Try different common encodings
    encodings_to_try = ['utf-8', 'windows-1252', 'iso-8859-1', 'ascii']
    print("\nTrying different encodings:")
    for encoding in encodings_to_try:
        try:
            decoded = content.decode(encoding)
            print(f"{encoding}: Successfully decoded")
            # Show a small sample of decoded text
            print(f"Sample text: {decoded[:50]}")
        except UnicodeDecodeError as e:
            print(f"{encoding}: Failed - {str(e)}")
    
if __name__ == '__main__': 
    file_path = Path(r'C:\npp-ide\Dashboard\projects\mf-file-processor\dist\T659J4.txt')    
    file_path_formatted = file_path.parent / f"{file_path.stem}_{file_path.suffix}"
    file_path_formatted_ = file_path.parent / f"{file_path.stem}__{file_path.suffix}"
    # inspect_file_encoding(file_path)
    print(f"Processing file: {file_path}")
    
    # primary conversion to utf-8 to add some starting bytes as
    # after the first iteration, you need to check if there is any � character in the _ file, which not possible to convert to utf-8.
    # if there are some �'s; you need the find out corresponding hex values in the initial file  
    
    # 1. first iteration, convert from 8 byte set to utf-8 
    linelist = readfile_cp1252(file_path)
    writefile(file_path_formatted, linelist) 
       
    # 2. second iteration, fix utf-8 errors with binary conversion.
    linelist = readfile_binary(file_path_formatted)
    linelist = process_bad_chars(linelist)
    
    writefile(file_path_formatted_, linelist)  

