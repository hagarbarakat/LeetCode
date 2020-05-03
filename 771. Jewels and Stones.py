class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        s = set(J)
        ans = 0 
        for i in S:
            if i in s: 
                ans += 1
        return ans
----------------------------------------------------------
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0
        for i in S: 
            for j in J:
                if i == j:
                    ans += 1
        return ans