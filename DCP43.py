# Daily Coding Problem # 43
#
# Implement a stack that has the following methods:
# 
#     push(val), which pushes an element onto the stack
#     pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
#     max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
# 
# Each method should run in constant time.

# Questions
# Do I have the .append() method available?
#    Assume: Yes
# When the stack is constructed, is only one value being added at a time?
#    Assume: Will always start with 0 or 1 element in the stack.
# Does it matter which element we remove when "pop"ing?
#    Assume: pop off the last entry.
# Am I allowed to use additional storage space?
#    Assume: Yes

class Stack:
    def __init__(self, value=[]):
        self.stack = value.copy()
        self.max_list = value.copy()
        
        
    def push(self, val):
        self.stack.append(val)
        if len(self.max_list) == 0:
            self.max_list.append(val)
        elif val >= self.max_list[len(self.max_list) - 1]:
            self.max_list.append(val)
    
    def pop(self):
        if len(self.stack) == 0:
            print("There is nothing in the stack to pop.")
            return None
        tmp = self.stack[len(self.stack) - 1]
        if tmp == self.max_list[len(self.max_list) - 1]:
            del self.max_list[len(self.max_list) - 1]
        del self.stack[len(self.stack) - 1]
        
    def max(self):
        if len(self.stack) == 0:
            print("There is no stack to get the maximum value of.")
            return None
        print(self.max_list)
        print(self.max_list[len(self.max_list) - 1])
        return self.max_list[len(self.max_list) - 1]
