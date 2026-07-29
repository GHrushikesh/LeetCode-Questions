# #1920 - 1920. Build Array from Permutation

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `5` |
| **Memory** | `19552000` |
| **Topic Tags** | `Array, Simulation` |
| **Date** | `2026-07-15 19:30` |

## Solution

```python3
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        n = len(nums)

        for i in range(n):
            nums[i] += n * (nums[nums[i]] % n)

        for i in range(n):
            nums[i] //= n

        return nums
```

---
*Generated automatically by [RG Sync](https://github.com).*