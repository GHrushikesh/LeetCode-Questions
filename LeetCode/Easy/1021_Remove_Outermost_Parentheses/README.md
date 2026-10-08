# #1021 - 1021. Remove Outermost Parentheses

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `4` |
| **Memory** | `19352000` |
| **Topic Tags** | `String, Stack, Bracket Sequences` |
| **Date** | `2026-10-08 21:32` |

## Solution

```python3
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        balance = 0

        for ch in s:
            if ch == '(':
                if balance > 0:
                    result += ch
                balance += 1

            else:
                balance -= 1
                if balance > 0:
                    result += ch

        return result
```

---
*Generated automatically by [RG Sync](https://github.com).*