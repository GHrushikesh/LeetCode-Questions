# #66 - 66. Plus One

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19388000` |
| **Topic Tags** | `Array, Math` |
| **Date** | `2026-07-30 18:39` |

## Solution

```python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits
```

---
*Generated automatically by [RG Sync](https://github.com).*