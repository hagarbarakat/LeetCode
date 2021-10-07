class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0 
        j = int(len(nums)/2) 
        output = []
        while j < len(nums): 
            output.append(nums[i])
            output.append(nums[j])
            i += 1
            j += 1
        return output 
    #----------------------------------------------------
    