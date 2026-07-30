# #844 - 844. Backspace String Compare

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19236000` |
| **Topic Tags** | `Two Pointers, String, Stack, Simulation` |
| **Date** | `2026-07-30 19:07` |

## Solution

```python3
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack = []

            for ch in string:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)

            return stack

        return build(s) == build(t)
```

---
*Generated automatically by [RG Sync](https://github.com).*