# #1541 - 1541. Minimum Insertions to Balance a Parentheses String

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `87` |
| **Memory** | `20072000` |
| **Topic Tags** | `String, Stack, Greedy, Bracket Sequences` |
| **Date** | `2026-10-09 18:00` |

## Solution

```python3
class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        open_count = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open_count += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    ans += 1

                if open_count > 0:
                    open_count -= 1
                else:
                    ans += 1

            i += 1

        ans += open_count * 2

        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*