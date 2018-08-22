# Daily Coding problem # 45
#
# This problem was asked by Two Sigma.
# 
# Using a function rand5() that returns an integer from 1 to 5 (inclusive) 
# with uniform probability, implement a function rand7() that returns an 
# integer from 1 to 7 (inclusive).


def rand5():
    # returns a number 1-5 randomly
    pass
    
    
def rand7():
    return (rand5() + rand5()) mod 7 + 1
    
    
    
