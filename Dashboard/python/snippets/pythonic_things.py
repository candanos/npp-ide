# pythonics:
    # comprehensions: 
        '''
        A list comprehension is a compact way to create a new list based on existing iterables. 
        It provides a shorter syntax when you want to create a new list based on the values of an existing list 
        or when you want to generate a list by applying some operations or filtering on elements.
        '''
    # 1. Simple list comprehension:
        squares = [x**2 for x in range(10)]
        # Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]    
    # 2. List comprehension with a condition:
        even_squares = [x**2 for x in range(10) if x % 2 == 0]
        # Result: [0, 4, 16, 36, 64]
    # 3. Nested list comprehension. Merge multiple lists in a single line.
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        flattened = [num for row in matrix for num in row]
        # Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = [True, False, True]
        merged_list = [item for sublist in (list1, list2, list3) for item in sublist]
        # Output: [1, 2, 3, 'a', 'b', 'c', True, False, True]
        
        directory = r'C:\npp-ide\Dashboard'
        extensions = ['ps1', 'py']
        mylist = [ file for ext in extensions for file in directory.rglob(f'*{ext}')]
        for x in mylist:
            print(x)