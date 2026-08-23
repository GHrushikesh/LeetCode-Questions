# #567 - 567. Permutation in String

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `15` |
| **Memory** | `19352000` |
| **Topic Tags** | `Hash Table, Two Pointers, String, Sliding Window` |
| **Date** | `2026-08-23 15:53` |

## Solution

```python3
class Solution:
    def isFreqSame(self, freq1, freq2):
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        for ch in s1:
            index = ord(ch) - ord('a')
            freq1[index] += 1
        windowSize = len(s1)
        for i in range(windowSize):
            index = ord(s2[i]) - ord('a')
            freq2[index] += 1
        if self.isFreqSame(freq1, freq2):
            return True
        left = 0
        for right in range(windowSize, len(s2)):
            removeIndex = ord(s2[left]) - ord('a')
            freq2[removeIndex] -= 1
            addIndex = ord(s2[right]) - ord('a')
            freq2[addIndex] += 1
            left += 1
            if self.isFreqSame(freq1, freq2):
                return True
        return False
```

---
*Generated automatically by [RG Sync](https://github.com).*