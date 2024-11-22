import re

def check_sequence(text):
    # Pattern explanation:
    # IF\s+ - matches 'IF' followed by one or more whitespace characters
    # (\w+-)?XYZDOM - matches optional word characters followed by hyphen, then XYZDOM
    # \s+ - matches one or more whitespace characters
    # = - matches the equals sign
    pattern = r'IF\s+(\w+-)?XYZDOM\s+='
    
    match = re.search(pattern, text)
    return bool(match)

# Test cases
test_strings = [
    "IF XYZDOM =",           # Valid (no prefix)
    "IF PRE-XYZDOM =",       # Valid (with prefix)
    "IF ABC-XYZDOM =",       # Valid (different prefix)
    "IF TEST123-XYZDOM =",   # Valid (alphanumeric prefix)
    "IF -XYZDOM =",          # Invalid (hyphen without prefix)
    "IF PREXYZDOM =",        # Invalid (no hyphen)
    "IF PRE-XYZDOM=",        # Invalid (no space before =)
    "IFPRE-XYZDOM =",        # Invalid (no space after IF)
    "PRE-XYZDOM IF =",       # Invalid (wrong order)
    " IF W-XYZDOM = 'SD'",   # Valid
]
for test in test_strings:
    print(f"'{test}': {check_sequence(test)}")