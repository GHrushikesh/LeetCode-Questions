# #228 - 228. Summary Ranges

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19272000` |
| **Topic Tags** | `Array` |
| **Date** | `2026-07-27 20:56` |

## Solution

```python3
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        n = len(nums)
        i = 0

        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1

            end = nums[i]

            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))

            i += 1

        return result
```

---
*Generated automatically by [RG Sync](https://github.com).*