from pathlib import Path
import re 

def list_files(directory):
    directory_path = Path(directory)
    return [file for file in directory_path.rglob('*') if file.is_file()]

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

# Specify the directory you want to list files for
directory_to_list = 'C:/github/kola-cobol/cobol' 

# Get the list of all files
cobolpaths = list_files(directory_to_list)
reportpath = 'C:/github/kola-cobol/report.txt'
reportfile = open(reportpath, "w")

# Print the list of files
print(f"{len(cobolpaths)} is found in the directory!" )
allreportlines = []
for cobolpath in cobolpaths:
    cobolfile = open(cobolpath, "r")
    cobollines = cobolfile.read().split('\n')
    returnlines = check_password_keyword(cobollines)
    if returnlines:
        allreportlines.append(f">>{cobolpath}<<")
        allreportlines.extend(returnlines)
        
for line in allreportlines:
    reportfile.write(line + '\n')    
reportfile.close()    