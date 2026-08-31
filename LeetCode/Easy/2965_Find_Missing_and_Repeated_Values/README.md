# #2965 - 2965. Find Missing and Repeated Values

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `7` |
| **Memory** | `19532000` |
| **Topic Tags** | `Array, Hash Table, Math, Matrix` |
| **Date** | `2026-08-31 19:54` |

## Solution

```python3
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = [0] * (n * n + 1)

        for row in grid:
            for num in row:
                freq[num] += 1

        repeated = 0
        missing = 0

        for num in range(1, n * n + 1):
            if freq[num] == 2:
                repeated = num
            elif freq[num] == 0:
                missing = num

        return [repeated, missing]
```

---
*Generated automatically by [RG Sync](https://github.com).*