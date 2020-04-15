class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = []
        temp = 1
        for i in range(len(nums)):
            prod.append(1)
        print(prod)
        for i in range(len(nums)):
            prod[i] = temp
            temp *= nums[i]
        temp = 1
        i = len(nums)-1
        while i >= 0:
            prod[i] *= temp
            temp *= nums[i]
            i -= 1
        return prod
            