# #3 - 3. Longest Substring Without Repeating Characters

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `211` |
| **Memory** | `19872000` |
| **Topic Tags** | `Hash Table, String, Sliding Window` |
| **Date** | `2026-08-15 14:00` |

## Solution

```python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Remove characters until s[right] is unique
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
```

---
*Generated automatically by [RG Sync](https://github.com).*