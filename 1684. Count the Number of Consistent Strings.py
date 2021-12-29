class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)
        ans = 0
        for word in words:
            for char in word:
                if char not in a:
                    ans += 1
                    break
        return len(words) - ans
