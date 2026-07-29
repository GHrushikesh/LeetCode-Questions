# #448 - 448. Find All Numbers Disappeared in an Array

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `22` |
| **Memory** | `30468000` |
| **Topic Tags** | `Array, Hash Table` |
| **Date** | `2026-07-27 18:09` |

## Solution

```python3
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans =[]
        num_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in num_set:
                ans.append(i)
        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*