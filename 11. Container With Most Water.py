class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0 
        end = len(height) - 1
        maximum = float("-inf")
        while start < end:
            mini = min(height[start], height[end])
            area = (end - start) * mini
            maximum = max(maximum, area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maximum