# #729 - 729. My Calendar I

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `239` |
| **Memory** | `20168000` |
| **Topic Tags** | `Array, Binary Search, Design, Segment Tree, Ordered Set` |
| **Date** | `2026-06-18 16:40` |

## Solution

```python3
class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:

        for event in self.events:
            oldStart, oldEnd = event

            if startTime < oldEnd and endTime > oldStart:
                return False

        self.events.append((startTime, endTime))
        return True
```

---
*Generated automatically by [RG Sync](https://github.com).*