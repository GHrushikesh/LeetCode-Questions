# #46 - 46. Permutations

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `3` |
| **Memory** | `19640000` |
| **Topic Tags** | `Array, Backtracking` |
| **Date** | `2026-10-06 16:16` |

## Solution

```python3
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        current = []
        used = [False] * len(nums)
        def backtrack():
            if len(nums) == len(current):
                temp = []
                for value in current:
                    temp.append(value)
                result.append(temp)
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                current.append(nums[i])
                backtrack()
                current.pop()
                used[i] = False
        backtrack()
        return result
```

---
*Generated automatically by [RG Sync](https://github.com).*