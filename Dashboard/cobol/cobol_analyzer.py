from pathlib import Path
import re 


def list_files(directory):
    directory_path = Path(directory)
    return [file for file in directory_path.rglob('T660*') if file.is_file()]


def check_password_keyword(cobollines):
    reportlines = []    
    # for cobolline in cobollines:
        # if re.search('password', cobolline, re.IGNORECASE):
            # if not re.search('W1010-PASSWORD', cobolline, re.IGNORECASE):
                # reportlines.append(cobolline)
    pattern1 = r"MOVE\s*(.*?)\s*TO\s*(.*?)\s*-PASSWORD"
    for cobolline in cobollines:
        match = re.search(pattern1, cobolline)
        if match:
            password = match.group(1)
            pattern2 = r"'(.*?)'"
            matches = re.findall(pattern2, password)
            if matches:
                reportlines.append(f"{cobolline} ::: {matches[0]}")
                
    return reportlines
    

def check_dcn_types(cobollines):
    pattern1 = r'(IF|AND|OR)\s+(\w+-)?KDAEOTYP\s+='
    pattern2 = r'\s+([\'"])[34]\1\s+'
    for i, cobolline in enumerate(cobollines):
        match = False
        if len(cobolline) > 6:
            if cobolline[6] != '*':
                match = bool(re.search(pattern1, cobolline))
                if match:
                    match = bool(re.search(pattern2, cobolline))
                    if match:
                        return cobolline.strip()
                    elif bool(re.search(pattern2, cobollines[i+1])):
                        return cobolline.strip()
    return None
                        
                    
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
    directory_to_list = r'C:\github\kola-cobol\cobol' 
    reportpath = r'C:\npp-ide\Dashboard\cobol\workspace\search_results.txt'
    reportfile = open(reportpath, "w+")
    rgx  = r'\bIDAVD\b\s+=\s+:\bT400-IDAVD\b' # updating a db2 field
    rgx  = r'IDAVD.*\b(IF|AND|OR)\b|\b(IF|AND|OR)\b.*IDAVD' # possible business rules for a field
    rgx  = r'\bMOVE\b.*\bTO\b.*\bW4IL1-KDBEHAND\b' # updating a parameter copy field
    rgx  = r'\bFROM\b\s+\bITEM_MARKFOR\b' # reading a db2 table


    search_in_directory_with_regex(directory_to_list, rgx)    
    