class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {"I" : 1, "V" : 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        output = hashmap.get(s[-1])
        for i in reversed(range(len(s) -1)): 
            if hashmap[s[i]] < hashmap[s[i + 1]]:
                output -= hashmap[s[i]]
            else: 
                output += hashmap[s[i]] 
        return output