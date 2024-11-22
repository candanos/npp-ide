import re

def find_quoted_number(text):
    # Pattern without anchors to find matches within text
    pattern = r'\s+([\'"])[34]\1\s+'
    
    # Using findall() to get all matches
    matches = re.findall(pattern, text)
    return bool(matches)  # Returns True if any matches found

# Test cases
test_strings = [
    "'3'",                  # Valid
    '"4"',                  # Valid
    " as '4' sdfdf ",      # Valid (contains '4')
    "testing \"3\" here",   # Valid (contains "3")
    "before '3' after",     # Valid (contains '3')
    "'5'",                  # Invalid (wrong number)
    "'3\"",                 # Invalid (different quotes)
    "no quotes 3 here",     # Invalid (no quotes)
    "lets '3'here",    # Invalid (no quotes)
    "lets '3' or '4' here",    # Invalid (no quotes)
    "lets'3' here"    # Invalid (no quotes)
]


for test in test_strings:
    print(f"'{test}': {find_quoted_number(test)}")