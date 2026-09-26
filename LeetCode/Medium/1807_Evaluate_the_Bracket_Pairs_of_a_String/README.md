# #1807 - 1807. Evaluate the Bracket Pairs of a String

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `47` |
| **Memory** | `51944000` |
| **Topic Tags** | `Array, Hash Table, String` |
| **Date** | `2026-09-26 19:08` |

## Solution

```python3
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)
        ans, start = [], -1
        for i, c in enumerate(s):
            if c == "(":
                start = i
            elif c == ")":
                ans.append(d.get(s[start + 1 : i], "?"))
                start = -1
            elif start < 0:
                ans.append(c)
        return "".join(ans)
```

---
*Generated automatically by [RG Sync](https://github.com).*