class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastpos = len(nums)-1
        i = len(nums)-1
        while i >=0:
            if i + nums[i] >= lastpos:
                lastpos = i
            i -= 1
        return lastpos == 0