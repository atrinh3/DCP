# Daily Coding Problem # 47
#
# Given a array of numbers representing the stock prices of a 
# company in chronological order, write a function that calculates 
# the maximum profit you could have made from buying and selling 
# that stock once. You must buy before you can sell it.
# 
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, 
# since you could buy the stock at 5 dollars and sell it at 10 dollars.

# Questions:
# What if there is only 1 point in the array?
    # Assume: That will never happen. There will always be >=2 elements.
# What if the array only goes down? i.e. no opportunity for gain.
    # Assume: Return 0

def most_profit(a):
    mn = a[0]
    mx = 0
    current = 0
    save = 0
    
    for i in range(1, len(a)):
        if a[i] >= mn:
            if a[i] > mx:
                mx = a[i]
                current = mx - mn
        else:
            if current >= save:
                save = current
            mn = a[i]
            mx = 0
            current = 0
    if current > save:
        return current
    return save
        
