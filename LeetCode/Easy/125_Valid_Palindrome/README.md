# #125 - 125. Valid Palindrome

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `10` |
| **Memory** | `19732000` |
| **Topic Tags** | `Two Pointers, String` |
| **Date** | `2026-07-22 19:27` |

## Solution

```python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for ch in s:
            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
                new += ch.lower()

        return new == new[::-1]
```

---
*Generated automatically by [RG Sync](https://github.com).*