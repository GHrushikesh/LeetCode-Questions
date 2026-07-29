class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = {}
        for ch in sentence:
            letters[ch] = 1
        if len(letters) == 26:
            return True
        return False