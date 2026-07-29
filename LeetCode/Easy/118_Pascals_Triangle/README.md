# #118 - 118. Pascal's Triangle

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19288000` |
| **Topic Tags** | `Array, Dynamic Programming` |
| **Date** | `2026-07-29 18:09` |

## Solution

```python3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1 ,i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)
        return triangle
```

---
*Generated automatically by [RG Sync](https://github.com).*