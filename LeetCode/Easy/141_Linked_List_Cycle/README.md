# #141 - 141. Linked List Cycle

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `52` |
| **Memory** | `22568000` |
| **Topic Tags** | `Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm` |
| **Date** | `2026-08-08 15:36` |

## Solution

```python3
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast= head 
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

---
*Generated automatically by [RG Sync](https://github.com).*