# #240 - 240. Search a 2D Matrix II

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `140` |
| **Memory** | `25564000` |
| **Topic Tags** | `Array, Binary Search, Divide and Conquer, Matrix` |
| **Date** | `2026-08-30 22:09` |

## Solution

```python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            current = matrix[row][col]
            if current == target:
                return True
            elif current > target:
                col -= 1
            else:
                row += 1
        return False
```

---
*Generated automatically by [RG Sync](https://github.com).*