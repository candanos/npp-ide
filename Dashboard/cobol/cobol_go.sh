#!/bin/bash

WORKINGDIR=$1
COBOLFILES=$2

COBC_PATH="/c/msys64/mingw64/bin"


# export COBC_PATH="/c/Java/jdk1.8.0_261"
export PATH=$COBC_PATH:$PATH


cobc -c $COBOLFILES

echo "bye bye cobol_compiler.sh"
read -p "Press [Enter] key to go on."