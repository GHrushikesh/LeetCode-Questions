# #1614 - 1614. Maximum Nesting Depth of the Parentheses

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19212000` |
| **Topic Tags** | `String, Stack, Bracket Sequences` |
| **Date** | `2026-09-28 20:54` |

## Solution

```python3
class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for ch in s:
            if ch == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif ch == ')':
                depth -= 1
        return max_depth
```

---
*Generated automatically by [RG Sync](https://github.com).*