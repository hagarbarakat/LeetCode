class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(magazine) < len(ransomNote):
            return False
        dic = dict.fromkeys(magazine,0)
        for i in range(len(magazine)):
            if dic[magazine[i]] != 0:
                dic[magazine[i]] += 1
            else:
                dic[magazine[i]] = 1
        for i in ransomNote:
            if i in dic and dic[i] > 0:
                dic[i] -= 1
            else:
                return False
        return True
------------------------------------------------------------
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        if len(magazine) < len(ransomNote):
            return False
        r = sorted(ransomNote, reverse=True)
        m = sorted(magazine, reverse = True)
        while r and m: 
            if r[-1] == m[-1]:
                r.pop()
                m.pop()
            elif m[-1] < r[-1]:
                m.pop()
            else:
                return False
        return not r