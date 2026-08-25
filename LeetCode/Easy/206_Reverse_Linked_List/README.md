# #206 - 206. Reverse Linked List

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `20432000` |
| **Topic Tags** | `Linked List, Recursion` |
| **Date** | `2026-08-03 17:55` |

## Solution

```python3
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
```

---
*Generated automatically by [RG Sync](https://github.com).*