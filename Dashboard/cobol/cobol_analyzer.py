from pathlib import Path
import re 

# Specify the directory you want to list files for
directory_to_list = 'C:/github/kola-cobol/cobol' 
reportpath = 'C:/github/kola-cobol/report.txt'
reportfile = open(reportpath, "w")
allreportlines = []

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
                        
                    

if __name__ == "__main__":
    cobolpaths = list_files(directory_to_list)
    # Get the list of all files
    print(f"{len(cobolpaths)} is found in the directory!" )
    for cobolpath in cobolpaths:
        cobolfile = open(cobolpath, "r")
        # cobollines = cobolfile.read().split('\n')
        cobollines = cobolfile.readlines()
        # returnlines = check_password_keyword(cobollines)
        returnlines = check_dcn_types(cobollines)
        print(returnlines)
        if returnlines:
            allreportlines.append(f">>{cobolpath}<<")
            # allreportlines.extend(returnlines)
            allreportlines.append(f"{returnlines}")
            
    for line in allreportlines:
        reportfile.write(line + '\n')    
    reportfile.close()  