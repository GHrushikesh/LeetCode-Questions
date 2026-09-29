# #1143 - 1143. Longest Common Subsequence

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `334` |
| **Memory** | `44484000` |
| **Topic Tags** | `String, Dynamic Programming, Longest Common Subsequence` |
| **Date** | `2026-09-29 22:01` |

## Solution

```python3
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    first = dp[i - 1][j]
                    second = dp[i][j - 1]
                    if first > second:
                        dp[i][j] = first
                    else:
                        dp[i][j] = second
        return dp[n][m]
```

---
*Generated automatically by [RG Sync](https://github.com).*