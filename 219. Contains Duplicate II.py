class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashmap = {}
        for i in range(len(nums)):
            if not nums[i] in hashmap:
                hashmap[nums[i]] = i 
            else:
                diff = abs(hashmap[nums[i]] - i) 
                if diff <= k:
                    return True
                else:
                    hashmap[nums[i]] = i
        return False