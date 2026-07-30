# #1768 - 1768. Merge Strings Alternately

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `45` |
| **Memory** | `19124000` |
| **Topic Tags** | `Two Pointers, String` |
| **Date** | `2026-07-30 21:35` |

## Solution

```python3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                ans.append(word1[i])
            if i < len(word2):
                ans.append(word2[i])

        result = ""
        for ch in ans:
            result += ch

        return result
```

---
*Generated automatically by [RG Sync](https://github.com).*