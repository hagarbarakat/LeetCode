class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(numbers) - 1
        while low < high:
            s = numbers[low] + numbers[high]
            if s == target:
                return [low + 1, high + 1]
            elif s < target:
                low += 1
            else:
                high -= 1
                
        return[-1, -1]