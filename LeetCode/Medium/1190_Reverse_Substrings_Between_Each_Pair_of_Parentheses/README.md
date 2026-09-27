# #1190 - 1190. Reverse Substrings Between Each Pair of Parentheses

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `19` |
| **Memory** | `19156000` |
| **Topic Tags** | `String, Stack, Bracket Sequences` |
| **Date** | `2026-09-27 17:59` |

## Solution

```python3
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current = ""
        for ch in s:
            if ch == "(":
                stack.append(current)
                current = ""
            elif ch == ")":
                left = 0
                right = len(current) - 1
                chars = []
                for c in current:
                    chars.append(c)
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
                reversed_string = ""
                for c in chars:
                    reversed_string += c
                previous = stack.pop()
                current = previous + reversed_string
            else:
                current += ch
        return current
```

---
*Generated automatically by [RG Sync](https://github.com).*