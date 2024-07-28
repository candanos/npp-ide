import re
# Sample string
main_string = "12444  MOVE something TO W1010-PASSWORD err'"
main_string = "169900     MOVE '490628'                   TO WE240-PASSWORD"

# Regex pattern with grouping to capture text between keywords
pattern = r"MOVE\s*(.*?)\s*TO\s*(.*?)\s*-PASSWORD"

# Search for the match
match = re.search(pattern, main_string)
print(main_string)
if match:
    text_between_move_and_to = match.group(1)
    text_between_to_and_domdom = match.group(2)
    print(f"Text between MOVE and TO: {text_between_move_and_to}")
    print(f"Text between TO and DOMDOM: {text_between_to_and_domdom}")
else:
    print("No match found.")
    
pattern = r"'(.*?)'"

# Find all matches
matches = re.findall(pattern, main_string)

# Print the matches
for match in matches:
    print(f"Text between single quotes: {match}")