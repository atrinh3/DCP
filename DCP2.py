# Daily Coding Problem # 2
#
# Given an array of integers, return a new array such that each element at 
# index i of the new array is the product of all the numbers in the original 
# array except the one at i.
# 
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output 
# would be [2, 3, 6].
# 
# Follow-up: what if you can't use division?


class Solution:
    def __init__(self, a):
        self.ary = a
        
        
    def v1(self):
        # Iterate through each element, get the answer one at a time
        # O(N^2)
        out = []
        for i in range(0, len(self.ary)):
            product = 1
            for j in range(0, len(self.ary)):
                if i != j:
                    product *= self.ary[j]
            out.append(product)
        return out


    def v2(self):
        # Save the product, iterate through the array and divide by
        # the values at each index.
        # O(N)
        product = 1
        for i in range(0, len(self.ary)):
            product *= self.ary[i]
        out = []
        for i in range(0, len(self.ary)):
            out.append(product / self.ary[i])
        return out
        

    def v3(self):
        # Without division
        # Make a tree-type structure. At each element of the list, make a 
        # decision on whether or not to omit the number. If we decide to 
        # omit, then change a "omit" tag to False or "unavailable".
        # O(logn)
        def helper(a, index, product, omit, output):
            if index >= len(a):
                if len(output) < len(a):
                    output.append(product)
                return output
            tmp = product * a[index]
            if index < len(a):
                if omit:
                    output = helper(a, index + 1, product, False, output)
            output = helper(a, index + 1, tmp, omit, output)
            return output
        
        index = 0
        product = 1
        omit = True
        out = []
        out = helper(self.ary, index, product, omit, out)
        return out
