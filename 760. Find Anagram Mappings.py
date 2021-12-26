class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        ans = []
        for i in range(len(nums2)):
            hashmap[nums2[i]] = i
        for num in nums1:
            if num in hashmap:
                ans.append(hashmap[num])
        return ans
