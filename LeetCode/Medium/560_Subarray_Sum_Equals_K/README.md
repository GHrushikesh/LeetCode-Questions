# #560 - 560. Subarray Sum Equals K

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `30` |
| **Memory** | `21636000` |
| **Topic Tags** | `Array, Hash Table, Prefix Sum` |
| **Date** | `2026-09-22 18:42` |

## Solution

```python3
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:

        prefix = {0: 1}

        current_sum = 0
        ans = 0

        for num in nums:
            current_sum += num

            needed = current_sum - k

            if needed in prefix:
                ans += prefix[needed]

            if current_sum in prefix:
                prefix[current_sum] += 1
            else:
                prefix[current_sum] = 1

        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*