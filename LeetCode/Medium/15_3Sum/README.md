# #15 - 15. 3Sum

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `1109` |
| **Memory** | `22200000` |
| **Topic Tags** | `Array, Two Pointers, Sorting` |
| **Date** | `2026-09-02 16:01` |

## Solution

```python3
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:        
        n = len(nums)

        for i in range(n):
            smallest = i

            for j in range(i + 1, n):
                if nums[j] < nums[smallest]:
                    smallest = j
            nums[i], nums[smallest] = nums[smallest], nums[i]
        result = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result
```

---
*Generated automatically by [RG Sync](https://github.com).*