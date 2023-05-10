class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        alphabets_s = {}
        alphabets_t = {}

        for i in s:
            if i not in alphabets_s:
                alphabets_s[i] = 1
            else:
                alphabets_s[i] += 1
        
        for i in t:
            if i not in alphabets_t:
                alphabets_t[i] = 1
            else:
                alphabets_t[i] += 1

        if alphabets_s == alphabets_t:
            return True
        
        return False
