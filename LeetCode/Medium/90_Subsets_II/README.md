# #90 - 90. Subsets II

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19500000` |
| **Topic Tags** | `Array, Backtracking, Bit Manipulation` |
| **Date** | `2026-10-04 18:55` |

## Solution

```python3
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        current = []

        def backtrack(index):
            result.append(current.copy())

            for i in range(index, len(nums)):

                if i > index and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])

                backtrack(i + 1)

                current.pop()

        backtrack(0)

        return result
```

---
*Generated automatically by [RG Sync](https://github.com).*