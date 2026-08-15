# #169 - 169. Majority Element###

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `7` |
| **Memory** | `21152000` |
| **Topic Tags** | `Array, Hash Table, Divide and Conquer, Sorting, Counting` |
| **Date** | `2026-06-09 23:45` |

## Solution

```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mc = nums[0]
        count = 1
        for i in range (1 , len(nums)):
            if (nums[i] == mc):
                count += 1
            else:
                count -= 1
                if(count == 0 ):
                    mc = nums[i]
                    count = 1
        return mc
```

---
*Generated automatically by [RG Sync](https://github.com).*