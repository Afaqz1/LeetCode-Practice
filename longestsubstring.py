class Solution:
    def lengthofLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[1])
                l +=1
            charSet.add(s[r])
            res = max(res, r - 1 + 1)
        return res
