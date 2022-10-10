class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: 
            return ""
        pal = list(palindrome)
        for i in range(len(pal)//2):
            if pal[i] != 'a': 
                pal[i] = 'a'
                return "".join(pal)
        pal[-1] = 'b'
        return "".join(pal)