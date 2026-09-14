# #836 - 836. Rectangle Overlap

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19232000` |
| **Topic Tags** | `Math, Geometry` |
| **Date** | `2026-09-14 15:03` |

## Solution

```python3
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
         # check if either rectangle is actually a line
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or
            rec2[0] == rec2[2] or rec2[1] == rec2[3]):
            return False

        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top
```

---
*Generated automatically by [RG Sync](https://github.com).*