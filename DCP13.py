# Daily Coding Problem # 13
#
# Given an integer k and a string s, find the length of the longest substring
# that contains at most k distinct characters.
# 
# For example, given s = "abcba" and k = 2, the longest substring with k
# distinct characters is "bcb".

# Start at beginning
# Initial thought: best case is O(N)
# Should we worry about case sensitive or special chars?
#     assume no / no
# Initiate an empty dictionary
# For each new letter, as long as the length of the dictionary is less than k, 
# add it to the dictionary with the value being the index of the string that 
# the letter showed up in.  If the dictionary is "full" and a new letter is 
# found, remove the oldest letter and replace it with the new letter.
#
# Each time a letter needs to be removed, need to compare to see if the output
# string needs to be updated.

def longest_string(s, k):
    compare = {}
    minimum = 0
    out = ""
    length = len(out)
    
    def helper(a):
        result = []
        for key in a:
            result.append([a[key], key])
        return min(result)
   
    for i in range(0, len(s)):
        current = s[i]
        if current not in compare:
            if len(compare) < k:
                compare[current] = i
            else:
                # compare is full
                if (i - minimum) >= length:
                    out = s[minimum:i]
                    length = len(out)
                    tmp = helper(compare)
                    minimum = tmp[0] + 1
                    compare.pop(tmp[1])
                    compare[current] = i
        else:
            # current is in compare
            compare[current] = i
    if out == "":
        return s
    return out
    
    
string = "hjhgfjhhgfj"
test = 3
print(longest_string(string, test))
