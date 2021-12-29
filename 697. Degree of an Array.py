class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hashmap = {}
        min_sub_array = float("inf")
        max_len = float("-inf")
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]].append(i)
            else:
                hashmap[nums[i]] = list()
                hashmap[nums[i]].append(i)

        for value in hashmap.values():
            if len(value) > max_len:
                max_len = len(value)
                min_sub_array = value[-1] - value[0] + 1
            elif len(value) == max_len:
                min_sub_array = min(min_sub_array, (value[-1] - value[0] + 1))
        return min_sub_array
