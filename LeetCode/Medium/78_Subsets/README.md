# #78 - 78. Subsets

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19292000` |
| **Topic Tags** | `Array, Backtracking, Bit Manipulation` |
| **Date** | `2026-09-29 21:50` |

## Solution

```python3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def backtrack(index):
            if index == len(nums):
                result.append(current.copy())
                return
            backtrack(index + 1)
            current.append(nums[index])
            backtrack(index + 1)
            current.pop()
        backtrack(0)
        return result
```

---
*Generated automatically by [RG Sync](https://github.com).*