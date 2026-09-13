# #835 - 835. Image Overlap

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `348` |
| **Memory** | `19792000` |
| **Topic Tags** | `Array, Matrix` |
| **Date** | `2026-09-13 15:03` |

## Solution

```python3
import collections

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        ones1 = []
        ones2 = []

        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones1.append((r, c))
                if img2[r][c] == 1:
                    ones2.append((r, c))

        shift_counts = collections.Counter()
        max_overlap = 0

        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2 - c1)
                shift_counts[shift] += 1
                max_overlap = max(max_overlap, shift_counts[shift])

        return max_overlap
```

---
*Generated automatically by [RG Sync](https://github.com).*