# Daily Coding Problem # 22
#
# Given a dictionary of words and a string made up of those words 
# (no spaces), return the original sentence in a list. If there is 
# more than one possible reconstruction, return any of them. If there 
# is no possible reconstruction, then return null.
# 
# For example, given the set of words 'quick', 'brown', 'the', 'fox', 
# and the string "thequickbrownfox", you should return ['the', 'quick', 
# 'brown', 'fox'].
# 
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', 
# and the string "bedbathandbeyond", return either ['bed', 'bath', 
# 'and', 'beyond] or ['bedbath', 'and', 'beyond'].


class CrazyString:
    def __init__(self, s="", s_set=[]):
        self.string = s
        self.string_set = s_set
    
    def v1(self):
        out = []
        start = 0
        for i in range(0, len(self.string)):
            tmp = self.string[start:i + 1]
            print(tmp)
            for word in self.string_set:
                if tmp == word:
                    out.append(word)
                    start = i + 1
        if start == len(self.string):
            return out
        return None
