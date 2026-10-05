# #856 - 856. Score of Parentheses

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19052000` |
| **Topic Tags** | `String, Stack, Bracket Sequences` |
| **Date** | `2026-10-05 19:15` |

## Solution

```python3
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = bal = 0
        for i, char in enumerate(s):
            if char == '(':
                bal += 1
            else:
                bal -= 1
                if s[i-1] == '(':
                    ans += 1 << bal
        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*