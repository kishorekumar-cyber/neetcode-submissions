class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        base = ord("a")
        for i in range(len(s)):
            count[ord(s[i]) - base] +=1
            count[ord(t[i]) -base] -=1
        return count==[0] * 26