class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setof = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in setof:
                setof.remove(s[l])
                l+=1
            setof.add(s[r])
            
            res = max(res, r-l+1)
        return res