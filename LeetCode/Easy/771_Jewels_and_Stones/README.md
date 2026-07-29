# #771 - 771. Jewels and Stones

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19248000` |
| **Topic Tags** | `Hash Table, String` |
| **Date** | `2026-07-19 14:39` |

## Solution

```python3
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count
```

---
*Generated automatically by [RG Sync](https://github.com).*