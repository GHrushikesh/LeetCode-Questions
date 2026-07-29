# #1108 - 1108. Defanging an IP Address

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `46` |
| **Memory** | `19428000` |
| **Topic Tags** | `String` |
| **Date** | `2026-07-19 14:34` |

## Solution

```python3
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for ch in address:
            if ch == ".":
                ans += "[.]"
            else:
                ans += ch
        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*