# notice that it adds spaces to reach the number of characters specified by width
In [1]: f'{1 + 3 * 1.5:10.3f}'
Out[1]: '     5.500'

# notice that it uses more characters than the ones specified in width
In [2]: f'{3000 + 3 ** (1 / 2):2.1f}' 
Out[2]: '3001.7'

In [3]: f'{1.2345 + 4 ** (1 / 2):9.6f}'
Out[3]: ' 3.234500'

# omitting width but providing precision will use the required characters to display the number with the the specified decimal places
In [4]: f'{1.2345 + 3 * 2:.3f}' 
Out[4]: '7.234'

# not specifying the format will display the number with as many digits as Python calculates
In [5]: f'{1.2345 + 3 * 0.5}'
Out[5]: '2.7344999999999997'