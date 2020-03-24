# str.find(sub,start,end)
# sub : It’s the substring which needs to be searched in the given string.
# start : Starting position where sub is needs to be checked within the string.
# end : Ending position where suffix is needs to be checked within the string. 

word = 'geeks for geeks'
  
# returns first occurrence of Substring 
result = word.find('geeks') 
print ("Substring 'geeks' found at index:", result ) 
  
result = word.find('for') 
print ("Substring 'for ' found at index:", result ) 
  
# How to use find() 
if (word.find('pawan') != -1): 
    print ("Contains given substring ") 
else: 
    print ("Doesn't contains given substring") 


word = 'geeks for geeks'
  
# Substring is searched in 'eks for geeks'  
print(word.find('ge', 2))  
  
# Substring is searched in 'eks for geeks'  
print(word.find('geeks ', 2))  
  
# Substring is searched in 's for g'  
print(word.find('g', 4, 10))  
  
# Substring is searched in 's for g'  
print(word.find('for ', 4, 11))  
