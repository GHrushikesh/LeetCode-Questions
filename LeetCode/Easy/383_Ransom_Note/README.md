# #383 - 383. Ransom Note

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `32` |
| **Memory** | `19540000` |
| **Topic Tags** | `Hash Table, String, Counting` |
| **Date** | `2026-07-27 18:02` |

## Solution

```python3
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for ch in magazine:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        for ch in ransomNote:   
            if ch not in count or count[ch] == 0:
                return False 
            count[ch] -= 1
        return True
```

---
*Generated automatically by [RG Sync](https://github.com).*