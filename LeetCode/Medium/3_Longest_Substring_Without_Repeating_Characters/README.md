# #3 - 3. Longest Substring Without Repeating Characters

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Java` |
| **Runtime** | `5` |
| **Memory** | `44752000` |
| **Topic Tags** | `Hash Table, String, Sliding Window` |
| **Date** | `2025-09-30 15:16` |

## Solution

```java
import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int left = 0, maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);

            // If character already seen, move left pointer
            if (map.containsKey(c)) {
                left = Math.max(left, map.get(c) + 1);
            }

            map.put(c, right); // store/update the index of current char
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}
```

---
*Generated automatically by [RG Sync](https://github.com).*