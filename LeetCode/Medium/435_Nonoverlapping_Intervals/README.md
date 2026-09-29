# #435 - 435. Non-overlapping Intervals

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `84` |
| **Memory** | `48996000` |
| **Topic Tags** | `Array, Dynamic Programming, Greedy, Sorting` |
| **Date** | `2026-09-29 22:07` |

## Solution

```python3
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removals = 0
        end_time = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end_time:
                removals += 1
            else:
                end_time = intervals[i][1]
        return removals
```

---
*Generated automatically by [RG Sync](https://github.com).*