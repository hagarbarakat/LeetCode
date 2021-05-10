class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dictionary = set()
        for i in range(len(nums)):
            if nums[i] in dictionary:
                return nums[i]
            else:
                dictionary.add(nums[i])