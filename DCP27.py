# Daily Coding Problem # 27
#
# Given a string of round, curly, and square open and closing brackets, 
# return whether the brackets are balanced (well-formed).
# 
# For example, given the string "([])[]({})", you should return true.
# 
# Given the string "([)]" or "((()", you should return false.

# Questions:
# Can I assume the string will consist only of correct symbols every time?
#    Assuming yes


# Create a stack.  Each time a beginning bracket is found, store it in the stack.
# When a closing bracket is found, check for matching pair at the top of the newly
# made stack.  If it doesn't match, return False.  Otherwise, if they match, then
# just remove the opening bracket from the top of the newly made stack.
def is_balanced(s):
    stack = []
    for i in range(0, len(s)):
        current = s[i]
        if current == "(" or current == "[" or current == "{":
            stack.append(current)
        else:
            opening = stack.pop(len(stack) -1)
            if current == ")":
                if opening != "(":
                    return False
            if current == "]":
                if opening != "[":
                    return False
            if current == "}":
                if opening != "{":
                    return False
    return stack == []
    
    
