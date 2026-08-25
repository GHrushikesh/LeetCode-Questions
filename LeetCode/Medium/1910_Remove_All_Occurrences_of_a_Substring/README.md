# #1910 - 1910. Remove All Occurrences of a Substring

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `3` |
| **Memory** | `19208000` |
| **Topic Tags** | `String, Stack, Simulation` |
| **Date** | `2026-08-06 21:42` |

## Solution

```python3
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for ch in s:
            stack.append(ch)
            if len(stack) >= len(part):
                match = True
                for i in range(len(part)):
                    if stack[len(stack) - len(part) + i] != part[i]:
                        match = False
                        break
                if match:
                    for i in range(len(part)):
                        stack.pop()
        ans = ""
        for ch in stack:
            ans += ch
        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*