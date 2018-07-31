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
        # Iterate through each letter
        # With each letter, compare with every word in the bank
        # If there's a match, add to the output list and reset starting point
        # Once you get to the end, if there are letters in the temporary word,
        # then it means that there are leftover letters that didn't match.
        out = []
        start = 0
        for i in range(0, len(self.string)):
            tmp = self.string[start:i + 1]
            for word in self.string_set:
                if tmp == word:
                    out.append(word)
                    start = i + 1
        if start == len(self.string):
            return out
        return None
    
    
    def v2(self):
        # Iterate through each letter.
        # As you go through the letters, check the word bank.
        # Remove words from the word bank as they don't become applicable
        # Once a word is found, restore the word bank.
        # If the word bank is ever empty, return null/None right away.
        # Sacrifices a little bit of memory since have to make a copy of the
        # word bank list.
        out = []
        start = 0
        bank = self.string_set.copy()
        for i in range(0, len(self.string)):
            if len(bank) == 0:
                return None
            tmp = self.string[start:i + 1]
            del_count = 0
            for j in range(0, len(bank)):
                word = bank[j - del_count]
                if tmp == word:
                    out.append(word)
                    bank = self.string_set.copy()
                    start = i + 1
                    del_count = 0
                    break
                else:
                    if not self.string[start:].startswith(word):
                        del bank[j - del_count]
                        del_count += 1
        if start == len(self.string):
            return out
        return None
    
    
# Notes:
# 
# Setting list1 = list2 doesn't work as shown in v2 function.
# list1 = list2 is copying the reference so editing list2 will
# also change list1.  Have to do list1 = list2.copy()
