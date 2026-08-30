# #54 - 54. Spiral Matrix

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19328000` |
| **Topic Tags** | `Array, Matrix, Simulation` |
| **Date** | `2026-08-30 22:50` |

## Solution

```python3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result
```

---
*Generated automatically by [RG Sync](https://github.com).*