# Daily Coding Problem # 1
#
# Given a list of numbers and a number k, return 
# whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, 
# return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


# Possible questions:
# Possibility of negative numbers?

# First idea - nested loop
# Iterate through the list
#     For each element in the list, iterate everything after it
#         Check if it adds up to k
# This will take O(N^2)

# Second idea - Save information
# Iterate through the list
#     For each entry, modify a list of 0, and 1 based on value of 
#     diff of k and current value
#     Check if the index of the saved list is modified and return True if so.

# This won't work if negative numbers are involved.
def find_pairs(l, k):
    tmp = []
    for entry in l:
        # check if counterpart is present
        # add self to the list
        diff = k - entry
        if diff >= 0 and diff < len(tmp):
            print(diff)
            if tmp[diff] == 1:
                return True
            elif entry < len(tmp):
                tmp[entry] = 1
        if entry < len(tmp):
            tmp[entry] = 1
        else:
            # need to add more zeros
            # add a 1 at the end
            for i in range(0, entry - len(tmp)):
                tmp.append(0)
            tmp.append(1)
        print(tmp)
    return False
