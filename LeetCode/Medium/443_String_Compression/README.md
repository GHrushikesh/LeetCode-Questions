# #443 - 443. String Compression

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `3` |
| **Memory** | `19412000` |
| **Topic Tags** | `Two Pointers, String` |
| **Date** | `2026-08-13 18:25` |

## Solution

```python3
class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        while read < len(chars):
            current = chars[read]
            count = 0
            while read < len(chars) and chars[read] == current:
                count += 1
                read += 1
            chars[write] = current
            write += 1
            if count > 1:
                count_str = str(count)
                for ch in count_str:
                    chars[write] = ch
                    write += 1
        return write
```

---
*Generated automatically by [RG Sync](https://github.com).*