#!/usr/bin/python
import sys
    
def array2lines(filePath, array):    
    f= open(filePath, "w+")
    for line in array:
        f.write(line)
    f.close()