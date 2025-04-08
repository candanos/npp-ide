import copybook
text = """
       01  WORK-BOOK.
        10  TAX-RATE        PIC S9(13)V9(2)
                    SIGN LEADING SEPARATE.
        10  AMOUNT        PIC S9(4)V9(2).
"""
text3 = """       
        01  T660C919.
            03 COMM-GEN-AREA.
                05 KOLA-MESSAGE.
                    07 IDUSER         PIC X(8).
                    07 PASSWORD       PIC X(8).
                    07 TIMESTAMP      PIC X(16).
                    07 KDOPER-CADREL  PIC X(8).
                    07 FILLER         PIC X(50).
                05 RETURN-MESSAGE.
                    07 KDRETUR        PIC X(3).
                    07 BEFEL          PIC X(200).
                    07 FILLER         PIC X(100).
"""                    

text2 = """
            01 COMM-DATA.
                05 KDMILJO           PIC X.
                05 IDAEONR           PIC X(8).
                05 KDAEOTYP          PIC X.
                05 IDUSER            PIC X(8).
                05 KDOPER-CADREL     PIC X(8).
                05 TIMESTAMP         PIC X(16).
                05 REVIEWERS.
                    07 GRRAD     PIC X(1600).         
                05 TXREASON-4 PIC X(320).                                            
                05 KDBOLAG           PIC X.
                05 SVAR.
                   07 RAD OCCURS 2 TIMES.              
                       09 IDINDAPX    PIC X(3).      
                       09 IDITEM      PIC X(8).      
                       09 KDUTGAVA    PIC X(3).      
                       09 KDARTKAT    PIC X.         
                       09 KDARTTYP2   PIC X(2).    
                       09 FLREJ       PIC X.        
                       09 FLCADREL    PIC X.         
                       09 KDOWNER-SYSTEM   PIC X(2).
                       09 KDLOMSKE    PIC X.         
                       09 TXEXTNAME   PIC X(50).     
                       09 IDEXTVERS   PIC X(20).     
                       09 KDEXTVAULT  PIC X(2).      
                       09 KDSTATUS-BRIDGE    PIC X.  
                       09 IDEXTOBJECT PIC X(200).    
                       09 FILLER      PIC X(50).  

""" 

                       
# copybook also provides a parse_file method that receives a text filename
root = copybook.parse_string(text)

# flatten returns a list of Fields and FieldGroups instead of traversing the tree
list_of_fields = root.flatten()

# dummy sample input
line = "          -13452987654"

# loop over the fields and parse the relevant position in the line
for field in list_of_fields:

  # FieldGroups are Copybook groups and contain Field objects as children
  if type(field)==copybook.Field:

    # each Field has a start_pos and a get_total_length method
    # to identify the position within the raw line input
    str_field = line[field.start_pos:field.start_pos+field.get_total_length()]

    # Field provides a parse method that returns a str, int, or float based on the PIC
    print(f"{field.name}: {field.parse(str_field)}")
    
# copybook 2
    
root = copybook.parse_string(text2)    
list_of_fields = root.flatten()
for field in list_of_fields:
  # if type(field)==copybook.Field:
    print(f"{field.name}: {field.start_pos}: {field.start_pos + (field.get_total_length() - 1)}: {field.get_total_length()}")    
    
some_text = text2    

# Parse the copybook
root = copybook.parse_string(some_text)

# Debug function to explore the structure of a field
def explore_field(field, prefix=""):
    # Print all attributes of the field
    print(f"{prefix}Field name: {field.name}")
    print(f"{prefix}All attributes of field: {dir(field)}")
    
    # Print a few key attributes that might contain the information we need
    for attr in dir(field):
        if attr.startswith("__"):
            continue  # Skip internal attributes
        try:
            value = getattr(field, attr)
            print(f"{prefix}  {attr}: {value}")
        except:
            print(f"{prefix}  {attr}: <error accessing>")
    
    # If the field has children, explore them too
    if hasattr(field, 'children') and field.children:
        print(f"{prefix}Children of {field.name}:")
        for child in field.children:
            explore_field(child, prefix + "  ")
    
    
def process_fields(field, level=0):
    name = field.name
    
    # Use the correct attributes for your version of the package
    size = getattr(field, 'byte_length', 'N/A')  # Replace with actual attribute
    starting_byte = getattr(field, 'position', 'N/A')  # Replace with actual attribute
    
    indent = "  " * level
    print(f"{indent}Field: {name}, Size: {size}, Starting Byte: {starting_byte}")
    
    if hasattr(field, 'children') and field.children:
        for child in field.children:
            process_fields(child, level + 1)


# Explore the first field as an example
# if root.children:
    # explore_field(root.children[0])
    
# for field in root.children:
    # process_fields(field)            