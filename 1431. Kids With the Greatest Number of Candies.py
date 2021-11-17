class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies) - extraCandies
        result = []
        for i in range(len(candies)): 
            if candies[i] >= max_candies: 
                result.append(True)
            else: 
                result.append(False)
        return result
    #-------------------------------------------------------
    class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maximum = max(candies)
        for i in range(len(candies)): 
            if candies[i] + extraCandies >= maximum: 
                result.append(True)
            else: 
                result.append(False)
        return result