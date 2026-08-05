# #344 - 344. Reverse String

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `23312000` |
| **Topic Tags** | `Two Pointers, String` |
| **Date** | `2026-08-05 18:16` |

## Solution

```python3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
```

---
*Generated automatically by [RG Sync](https://github.com).*