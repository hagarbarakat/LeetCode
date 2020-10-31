class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1, p2 = -1, -1
        minDistance = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
            elif words[i] == word2:
                p2 = i 
            if p1 != -1 and p2 != -1:
                minDistance = min(minDistance, abs(p1-p2))
        return minDistance