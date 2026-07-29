# #242 - 242. Valid Anagram

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `16` |
| **Memory** | `19464000` |
| **Topic Tags** | `Hash Table, String, Sorting` |
| **Date** | `2026-07-21 17:11` |

## Solution

```python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        for ch in t:
            if ch not in count:
                return False 
            count[ch] -= 1
            
            if count[ch] < 0:
                return False
        return True
```

---
*Generated automatically by [RG Sync](https://github.com).*