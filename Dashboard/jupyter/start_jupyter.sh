
export PYTHON_PATH="/c/python/Python312"
export PATH="$PYTHON_PATH/Scripts":$PYTHON_PATH:$PATH
# $1=$(CURRENT_DIRECTORY)
# $2=$(FILE_NAME)
echo $1  
echo $2
fullpath=$1/$2
echo $fullpath  
# jupyter lab $fullpath
jupyter notebook $fullpath