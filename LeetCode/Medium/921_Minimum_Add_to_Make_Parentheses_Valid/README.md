# #921 - 921. Minimum Add to Make Parentheses Valid

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `3` |
| **Memory** | `19412000` |
| **Topic Tags** | `String, Stack, Greedy, Bracket Sequences` |
| **Date** | `2026-10-06 17:13` |

## Solution

```python3
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_adds_required = 0

        for c in s:
            if c == "(":
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_adds_required += 1
        return min_adds_required + open_brackets
```

---
*Generated automatically by [RG Sync](https://github.com).*