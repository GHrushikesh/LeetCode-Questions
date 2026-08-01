# #238 - 238. Product of Array Except Self

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `30` |
| **Memory** | `27768000` |
| **Topic Tags** | `Array, Prefix Sum` |
| **Date** | `2026-08-01 18:42` |

## Solution

```python3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        prefix = [1] * n
        sufix = [1] * n
        for i in range(1 ,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2 , -1, -1):
            sufix[i] = sufix[i+1] * nums[i+1]
        for i in range(n):
            ans[i] = prefix[i] * sufix[i]
        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*