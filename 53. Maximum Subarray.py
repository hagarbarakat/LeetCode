class Solution(object):
    def maxSubArray(self, nums):
        """
        Dynamic programming 
        :type nums: List[int]
        :rtype: int
        """
        maxi = nums[0]
        i = 1
        while i < len(nums):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            maxi = max(maxi, nums[i])
            i += 1
        return maxi