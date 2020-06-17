lst = ['lionel', 'messi', 'christiano', 'ronaldo']    

for i in range(10):
    print(i)
print('***********')

for i in lst:
    print(i)
print('***********')

for i in (2,10):
    print(i)
print('***********')

for i in range(2, len(lst)):
    print(lst[i])
print('***********') 

for i in range(0, len(lst), 2):
    print(lst[i]) 
print('***********')

for i in range(1,10,3):
    print(i)
print('***********')

someDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(someDict.get('model'))  