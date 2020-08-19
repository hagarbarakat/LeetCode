class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        array = S.split(" ")
        for i in range(len(array)):
            if array[i][0] in vowels:
                array[i] += "ma"
            else:
                letter = array[i][0]
                array[i] = array[i][1:]
                array[i] += letter + "ma"
            array[i] += "a" * (i + 1)
        return " ".join(array)
        