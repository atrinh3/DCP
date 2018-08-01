# Daily Coding Problem # 3
#
# Given the root to a binary tree, implement serialize(root), 
# which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.
# 
# For example, given the following Node class
# 
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# The following test should pass:
# 
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
# In order to serialize, would like to traverse the tree going
# left to right. Will need to use a special separator character.
# Will assume a comma will not be a possible character in 
# self.val.
def serialize(n):
    string = str(n.val + ",")
    if n.left == None:
        string = string + "None," 
    else:
        string = string + serialize(n.left)
    if n.right == None:
        string = string + "None," 
    else:
        string = string + serialize(n.right)
    return string
    
    
def deserialize(s):
    def de_helper(s, tracker):
        value = ""
        for i in range(tracker, len(s)):
            if s[i] == ",":
                value = s[tracker:i]
                break
        location = tracker + len(value)
        if value == "None":
            return [None, location]
        node = Node(value)
        [node.left, location] = de_helper(s, location + 1)
        [node.right, location] = de_helper(s, location + 1)
        return node, location
    [out, loc] = de_helper(s, 0)
    return out
