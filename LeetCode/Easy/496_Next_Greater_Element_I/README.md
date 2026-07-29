# #496 - 496. Next Greater Element I

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `15` |
| **Memory** | `19560000` |
| **Topic Tags** | `Array, Hash Table, Stack, Monotonic Stack` |
| **Date** | `2026-07-29 17:44` |

## Solution

```python3
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for num in nums1:
            index = nums2.index(num)
            next_greater = -1
            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    next_greater = nums2[i]
                    break

            ans.append(next_greater)

        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*