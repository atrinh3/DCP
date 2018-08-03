
# Daily Coding Problem 4
# 
# Given an array of integers, find the first missing positive integer 
# in linear time and constant space. In other words, find the lowest 
# positive integer that does not exist in the array. The array can 
# contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input 
# [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

import math

class MissingInteger:
    def __init__(self, param):
        self.array = param
       
       
    # Naive way - start from 1, iterate through the array to look for it.
    # Increment up until the a number doesn't show up.
    # O(N^2)
    def first_missing_v1(self):
        found = True
        start = 0
        while found:
            start += 1
            for i in range(0, len(self.array)):
                if self.array[i] == start:
                    found = True
                    break
                else:
                    found = False
        return start


    # Better way - Use a second array to keep track of the numbers that are
    # present.  The value of a missing number for an array of length n will
    # be limited by n. EX. array of length 5 will at most have a missing
    # number of 6.  All other possibilities are contained in 1-5.
    # For an array of length 5, initiate a second array of 0's of length 5.  
    # Iterate through the input array and for all numbers between 0-length+1, 
    # switch the corresponding index from 0 to a 1.  At the end, iterate 
    # through the second array until a 0 is found.  Return that index.
    def first_missing_v2(self):
        tmp = [0] * len(self.array)
        for i in range(0, len(tmp)):
            current = self.array[i]
            if current > 0 and current <= len(tmp):
                tmp[current - 1] = 1
        for i in range(0, len(tmp)):
            if tmp[i] == 0:
                return (i + 1)
        return (len(tmp) + 1)


    # Now trying to find a way to do it without using memory and saving a 
    # second array.
    # Step 1: Remove all elements of the array that are <= 0.
    # Step 2: With the remaining array, iterate through the elements.  With 
    #         element, change array[element] to be negative. May have to 
    #         shift everything to the left to be able to use index 0.  At
    #         the end, traverse through the final array and return the 
    #         first index with a positive value.
    def first_missing_v3(self):
        def get_valid(a):
            for element in a:
                if element <= 0:
                    a.remove(element)
            return a
        out = get_valid(self.array)
        for i in range(0, len(out)):
            if out[i] <= len(out):
                value = abs(out[i])
                out[value - 1] = abs(out[value - 1]) * -1
        for i in range(0, len(out)):
            if out[i] >= 0:
                return i + 1
        return len(out) + 1
