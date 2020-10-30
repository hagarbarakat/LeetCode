class Solution(object):
    def missingNumber(self, nums):
        length = len(nums)
        nums.sort()
        for i in range(length):
            if i != nums[i]:
                return i
        return length

#---------------------------------------------------------------
class Solution(object):
    def missingNumber(self, nums):
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        return missing