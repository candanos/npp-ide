#!/usr/bin/python
import sys
    
def array2lines(filePath, array):    
    f= open(filePath, "w+")
    for line in array:
        file.write(line)
    f.close()