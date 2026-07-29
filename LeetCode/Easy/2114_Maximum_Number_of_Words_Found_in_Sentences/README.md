# #2114 - 2114. Maximum Number of Words Found in Sentences

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19204000` |
| **Topic Tags** | `Array, String` |
| **Date** | `2026-07-19 21:52` |

## Solution

```python3
class Solution:
    def mostWordsFound(self, sentences):
        maximum = 0

        for sentence in sentences:
            words = sentence.split()
            count = len(words)

            if count > maximum:
                maximum = count

        return maximum
```

---
*Generated automatically by [RG Sync](https://github.com).*