export PYTHON_PATH="/c/python/Python312"
export PATH="$PYTHON_PATH/Scripts":$PYTHON_PATH:$PATH
echo $PATH
newnotebook="ALIAS"
targetdir="/c/github/notebooks"
# for Windows
targetdir=$(cygpath -w $targetdir)
echo $targetdir
python create_notebook.py $newnotebook $targetdir
