class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        numbers = set(nums)
        for num in numbers: 
            if num - 1 not in numbers: 
                current = num
                current_streak = 1 
                while current + 1 in numbers: 
                    current += 1 
                    current_streak += 1
            longest_streak = max(current_streak, longest_streak)
        return longest_streak