import sys
import nbformat as nbf
import os
notebook = sys.argv[1]
targetdir = sys.argv[2]

# Create a new notebook object
nb = nbf.v4.new_notebook()

# Define the cells for the new notebook
cells = [
    nbf.v4.new_markdown_cell("# My New Notebook"),
    nbf.v4.new_code_cell("print('Hello, World!')")
]

# Add the cells to the notebook
nb['cells'] = cells

# Specify the directory where you want to save the notebook
print(notebook)
# Define the full path for the new notebook
if targetdir:
    targetdir = os.path.join(f"{targetdir}", f"{notebook}")
else:    
    targetdir = os.path.join(f"{os.getcwd()}", f"{notebook}")

print(targetdir)
os.makedirs(targetdir, exist_ok=True)  # Create the directory if it doesn't exist
notebook_path = os.path.join(f"{targetdir}", f"{notebook}.ipynb")


# Write the notebook to the specified directory
with open(f"{notebook_path}", 'w') as f:
    nbf.write(nb, f)

print(f"Notebook created at {notebook_path}")
