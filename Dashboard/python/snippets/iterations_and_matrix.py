# enumerating
# In Python 3, enumerate is a built-in function that provides an elegant way to iterate over an iterable while also tracking the index or position of each element. It returns an iterator that generates pairs of index and value.
# basic syntax is as follows: 
# enumerate(iterable, start=0)

fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits, 12):
    print(index, fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)

# traversing a matrix
# To traverse a matrix in Python 3, you can use nested loops to iterate over the rows and columns. Here's an example of how you can traverse a matrix using a nested loop:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Traverse the matrix
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # Move to the next line after each row
