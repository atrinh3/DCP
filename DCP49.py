# Daily Coding Problem # 49
#
# Given an array of numbers, find the maximum sum of any contiguous 
# subarray of the array.
# 
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum 
# sum would be 137, since we would take elements 42, 14, -5, and 86.
# 
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since 
# we would not take any elements.
# 
# Do this in O(N) time.



# Once the sum goes negative, can throw away the current sum and start
# again at 0.

def max_sum(a):
    cum_sum = 0
    holder = 0
    for i in range(0, len(a)):
        tmp = cum_sum + a[i]
        if tmp < 0:
            cum_sum = 0
        else:
            if tmp > cum_sum:
                holder = tmp
            cum_sum = tmp
    return cum_sum
    
    
