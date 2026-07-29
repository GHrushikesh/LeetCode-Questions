# #1365 - 1365. How Many Numbers Are Smaller Than the Current Number

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `146` |
| **Memory** | `19212000` |
| **Topic Tags** | `Array, Hash Table, Sorting, Counting Sort` |
| **Date** | `2026-07-17 21:43` |

## Solution

```python3
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            ans.append(count)
        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*