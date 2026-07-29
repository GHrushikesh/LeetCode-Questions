class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for ch in s:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1 
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1