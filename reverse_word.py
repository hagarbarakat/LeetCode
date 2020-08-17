class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(' ')
        l1=[]
        for i in s:
            l1.append(i[::-1])
        return ' '.join(l1)

----------------------------------------------------------------

