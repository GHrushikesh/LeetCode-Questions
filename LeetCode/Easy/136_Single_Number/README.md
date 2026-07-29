# #136 - 136. Single Number

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `N/A` |
| **Topic Tags** | `Array, Bit Manipulation` |
| **Date** | `2026-07-29 17:07` |

## Solution

```python3
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num in count:
            if count[num] == 1:
                return num
```

---
*Generated automatically by [RG Sync](https://github.com).*