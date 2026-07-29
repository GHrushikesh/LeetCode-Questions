# #20 - 20. Valid Parentheses

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `3` |
| **Memory** | `19420000` |
| **Topic Tags** | `String, Stack` |
| **Date** | `2026-07-28 19:16` |

## Solution

```python3
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
```

---
*Generated automatically by [RG Sync](https://github.com).*