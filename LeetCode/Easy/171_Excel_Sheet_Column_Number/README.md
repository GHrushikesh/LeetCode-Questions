# #171 - 171. Excel Sheet Column Number

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19152000` |
| **Topic Tags** | `Math, String` |
| **Date** | `2026-08-02 18:12` |

## Solution

```python3
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        
        for ch in columnTitle:
            value = ord(ch) - ord('A') + 1
            ans = ans * 26 + value
        
        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*