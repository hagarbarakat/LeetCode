class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e', 'o', 'u', 'i', 'A', 'E', 'U', 'I', 'O'}
        p1 = 0 
        p2 = len(s) - 1
        s = list(s)
        while p1 < p2:
            if s[p1] in vowels and s[p2] in vowels:               
                s[p1], s[p2] = s[p2], s[p1] 
                p1 += 1
                p2 -= 1
            elif s[p1] in vowels:
                p2 -= 1
            elif s[p2] in vowels:
                p1 += 1
            else:
                p2 -= 1
                p1 += 1
        return "".join(s)
        