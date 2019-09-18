#cerner_2^5_2019

'''
Lambdas are simple anonymous (nameless) functions
Syntax:
    lambda (arguments): (expression to evaluate and return)
An example:
'''
lambda x: x*x # Returns x^2
(lambda x: x*x)(2) # Lambda immediately called with 2 as argument
'''
Useful for generating new functions...
'''
def multiplier(x):
    return lambda n: x*n
'''
Name your new function and call
multiplier() with the desired
value.
'''
double = multiplier(2)
triple = multiplier(3)
'''
You can now call these new functions
like so:
'''
double(10) # => 20
triple(10) # => 30
'''
Can also be called with this
interesting syntax:
'''
multiplier(3)(2) # => 3 * 2 = 6
'''
You can also pass another lambda to your lambda
'''
passing = lambda x, func: x + func(x)
passing(2, lambda x: x*x) # => 2 + 2^2 = 6
'''
Or have a lambda within a lambda
'''
nested = lambda x: lambda y: x + y
nested(1)(1) # => 1 + 1 = 2
'''
Commonly used with map, filter, & reduce
Here is a nice way to perform an
operation on a listwithout explicitly
writing a loop:
'''
intList = [1,2,3,4,5]
greeting = ['hello', 'cerner', 'associate']

list(map(lambda x: x.upper(), greeting)) # => ['HELLO', 'CERNER', 'ASSOCIATE']
# Shorthand for above statement:
[x.upper() for x in greeting]

list(map(lambda x: x*x, intList)) # => [1, 4, 9, 16, 25]
# Shorthand for above statement:
[x*x for x in intList]

list(filter(lambda x: isinstance(x, int), [1,'hello',2,'cerner',3,'associate'])) # => [1, 2, 3]
# Shorthand for above statement:
[x for x in intList if isinstance(x, int)]

from functools import reduce as reduce
reduce(lambda acc, val: acc + val, intList) # => 15
