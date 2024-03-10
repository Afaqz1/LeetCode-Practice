class Solution:
    def isPalindrome(self, s:str) -> bool:
        """newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]"""
        l, r = 0, len(s) - 1

        while l<r:
            while l < r and not self.alphaNum(s[1]):
                l+= 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[1].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True

    def alphaNum(self, c):
        (ord('A') <= ord(c) <= ord('Z') or
         ord('a') < ord(c) <= ord('z') or
         ord('0') < ord(c) <= ord('9')) 