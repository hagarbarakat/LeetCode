class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_num = 0 
        string = list(keysPressed)
        longest_pressed = string[0]
        for i in range(len(releaseTimes)): 
            if i == 0: 
                max_num = releaseTimes[i]
            else: 
                diff = releaseTimes[i] - releaseTimes[i-1]
                if diff > max_num: 
                    max_num = diff 
                    longest_pressed = string[i]
                elif diff == max_num: 
                    longest_pressed = max(longest_pressed, string[i])
        return longest_pressed