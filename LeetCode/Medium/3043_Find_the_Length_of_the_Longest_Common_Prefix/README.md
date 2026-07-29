# #3043 - 3043. Find the Length of the Longest Common Prefix

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python` |
| **Runtime** | `509` |
| **Memory** | `23932000` |
| **Topic Tags** | `Array, Hash Table, String, Trie` |
| **Date** | `2026-05-21 11:15` |

## Solution

```python
class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        prefixes = set()

        for num in arr1:
            s = str(num)

            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        ans = 0

        for num in arr2:
            s = str(num)

            for i in range(1, len(s) + 1):
                if s[:i] in prefixes:
                    ans = max(ans, i)

        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*