class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # using dict -> O(N) 
        a = dict()
        result = []
        for i in range(len(nums)):
            if nums[i] not in a:
                a[nums[i]]= 1
            else:
                a[nums[i]] = a[nums[i]] + 1
        d = sorted(a.items(),key=operator.itemgetter(1),reverse=True)
        for i in range(len(d)):
            if k > 0:
                k -= 1
                result.append(d[i][0])
        return result
-----------------------------------------------------------
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # heap -> O(N log k) 
        count = collections.Counter(nums) 
        result = heapq.nlargest(k, count.keys(), key=count.get)
        return result
