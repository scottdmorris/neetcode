class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = r = 0
        ans = len(t)
        while l < len(s) and r<len(t):
            if s[l] == t[r]:
                l +=1
                r +=1
                ans -=1
            else:
                l += 1
        
        return ans