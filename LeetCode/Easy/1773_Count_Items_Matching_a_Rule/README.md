# #1773 - 1773. Count Items Matching a Rule

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `23564000` |
| **Topic Tags** | `Array, String` |
| **Date** | `2026-07-19 21:58` |

## Solution

```python3
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0

        for item in items:
            if ruleKey == "type":
                if item[0] == ruleValue:
                    count += 1

            elif ruleKey == "color":
                if item[1] == ruleValue:
                    count += 1

            elif ruleKey == "name":
                if item[2] == ruleValue:
                    count += 1

        return count
```

---
*Generated automatically by [RG Sync](https://github.com).*