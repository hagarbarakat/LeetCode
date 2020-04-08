class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        for i in arr:
            if i + 1 in arr:
                result += 1
        return result