class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0 
        length = len(s)
        for i in range(len(t)):
            if length == 0: 
                break
            if s[j] == t[i]: 
                j += 1
                length -= 1
            
        return length == 0 