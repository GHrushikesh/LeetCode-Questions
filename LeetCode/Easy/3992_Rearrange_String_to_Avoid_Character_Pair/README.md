# #3992 - 3992. Rearrange String to Avoid Character Pair

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `1` |
| **Memory** | `19436000` |
| **Topic Tags** | `None` |
| **Date** | `2026-07-18 20:04` |

## Solution

```python3
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ans = []
        for ch in s:
            if ch == y:
                ans.append(ch)
        for ch in s:
            if ch != x and ch!= y:
                ans.append(ch)
        for ch in s:
            if ch == x:
                ans.append(ch)
        return "".join(ans)
```

---
*Generated automatically by [RG Sync](https://github.com).*