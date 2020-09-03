# time complexity -> O(n * m)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    k = j + 1 
                    flag = 0
                    while k < len(nums2):
                        if nums2[k] > nums2[j]:
                            arr.append(nums2[k])
                            flag = 1
                            break
                        else:
                            k += 1
                    if flag == 0:
                        arr.append(-1)
        return arr

#----------------------------------------------------------------
# time complexity -> O(n + m)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
            stack = []
            hashmap = {}
            res = []
            for i in range(len(nums2)):
                while len(stack) != 0 and stack[-1] < nums2[i]:
                    hashmap[stack.pop(-1)] = nums2[i]
                stack.append(nums2[i])
            while len(stack) !=  0:
                hashmap[stack.pop(-1)] = -1
            for i in range(len(nums1)):
                res.append(hashmap[nums1[i]])
            return res