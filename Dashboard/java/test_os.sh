#!/bin/bash

echo "OS Type: $OSTYPE"
echo "Uname: $(uname)"


if [[ "$(uname)" == "Linux" ]]; then
    echo "Linux system"
elif [[ "$(uname)" == *"CYGWIN"* ]]; then
    echo "Cygwin on Windows"
elif [[ "$(uname)" == *"MINGW"* ]]; then
    echo "MinGW on Windows"
elif [[ "$(uname)" == "Darwin" ]]; then
    echo "MacOS system"
fi