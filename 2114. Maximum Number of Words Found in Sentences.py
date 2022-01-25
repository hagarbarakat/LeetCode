class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_length = 0
        for sentence in sentences:
            sentence = sentence.split()
            max_length = max(max_length, len(sentence))
        return max_length
