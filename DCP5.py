# Daily Coding Problem # 5
#
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first 
# and last element of that pair. For example, car(cons(3, 4)) returns 3, and 
# cdr(cons(3, 4)) returns 4.
# 
# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.

# Take a created pair.
# Using the pair, create an anonymous function using a, b variables. Return a.
def car(pair):
    return pair(lambda a, b: a)
    
# Take a created pair.
# Using the pair, create an anonymous function using a, b variables. Return b.
def cdr(pair):
    return pair(lambda a, b: b)
