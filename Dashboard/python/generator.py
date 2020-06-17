#comprehessions in python 

# (<expression> for <var> in <iterable> [if <condition>])
# The syntax (<expression> for <var> in <iterable> [if <condition>]) specifies the general form for a generator comprehension. This produces a generator, whose instructions for generating its members are provided within the parenthetical statement.

# Written in a long form, the pseudo-code for

# (<expression> for <var> in <iterable> if <condition>)

# is:

# for <var> in <iterable>:
    # if bool(<condition>):
        # yield <expression>


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))
# This function returns a generator, using a generator comprehension. The generator returns the string sliced, from 0 + a multiple of the length of the chunks, to the length of the chunks + a multiple of the length of the chunks.

# You can iterate over the generator like a list, tuple or string - for i in chunkstring(s,n): , or convert it into a list (for instance) with list(generator).

def subStringGenerator(string, length):
    i = 0
    while True:
        yield string[i:i+length]
        i=i+length
    
if __name__ == '__main__':
    strComplete = "01234567890123456789"
    length = 3
    myGen = subStringGenerator(strComplete,length) 
    subStr = next(myGen)
    print(subStr)
    while (len(subStr) == length):
        print(subStr)
        subStr = next(myGen)