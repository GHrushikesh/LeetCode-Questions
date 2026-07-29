# #239 - 239. Sliding Window Maximum

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Hard` |
| **Language** | `Python3` |
| **Runtime** | `183` |
| **Memory** | `35200000` |
| **Topic Tags** | `Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue` |
| **Date** | `2026-07-09 21:56` |

## Solution

```python3
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()   
        ans = []

        for i in range(len(nums)):

            
            if q and q[0] <= i - k:
                q.popleft()

            
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*