class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_word = {}
        second_word = {}
        for i in s:
            if i in first_word.keys():
                first_word[i] = first_word[i]+1 
            else:
                first_word[i] = 1
        for i in t:
            if i in second_word.keys():
                second_word[i] += 1
            else:
                second_word[i] = 1
        for character, occurence in first_word.items():
            if second_word.get(character) != occurence:
                return 0
            second_word.pop(character)
        if len(second_word) == 0:
            return 1
        return 0
    
