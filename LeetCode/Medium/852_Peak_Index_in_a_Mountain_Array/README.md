# #852 - 852. Peak Index in a Mountain Array

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `31324000` |
| **Topic Tags** | `Array, Binary Search, Ternary Search` |
| **Date** | `2026-08-04 19:18` |

## Solution

```python3
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
```

---
*Generated automatically by [RG Sync](https://github.com).*