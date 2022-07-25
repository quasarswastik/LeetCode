class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            while left < right and not self.isAlphanumeric(s[left]):
                left += 1
            while right > left and not self.isAlphanumeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return 0
            left, right = left+1, right-1
        return 1
                
    
    def isAlphanumeric(self, character):
        if (ord('A') <= ord(character) <= ord('Z')) or (ord('a') <= ord(character) <= ord('z')) or (ord('0') <= ord(character) <= ord('9')):
            return 1
        return 0
