class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hashmap = {}
        string = ''
        for i in range(len(indices)): 
            hashmap[indices[i]] = s[i]
        for i in range(len(s)): 
            string += hashmap[i]
        return string
#--------------------------------------------------------------------
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string = ['' for x in indices]
        for i, x in enumerate(indices):
            string[x] = s[i]
        return ''.join(string)  