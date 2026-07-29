class Solution:
    def mostWordsFound(self, sentences):
        maximum = 0

        for sentence in sentences:
            words = sentence.split()
            count = len(words)

            if count > maximum:
                maximum = count

        return maximum