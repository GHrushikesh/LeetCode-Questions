# #1832 - 1832. Check if the Sentence Is Pangram

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19200000` |
| **Topic Tags** | `Hash Table, String` |
| **Date** | `2026-07-21 17:40` |

## Solution

```python3
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = {}
        for ch in sentence:
            letters[ch] = 1
        if len(letters) == 26:
            return True
        return False
```

---
*Generated automatically by [RG Sync](https://github.com).*