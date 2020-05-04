class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n, i = num, 1 
        while n:
            num = num ^ i #toggle 
            i = i << 1 # left shift
            n = n >> 1 # right shift
        return num