# #1480 - 1480. Running Sum of 1d Array

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19188000` |
| **Topic Tags** | `Array, Prefix Sum` |
| **Date** | `2026-07-16 17:51` |

## Solution

```python3
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        ans = []
        for num in nums:
            total += num
            ans.append(total)

        print(total)        

        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*