# #147 - 147. Insertion Sort List

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `388` |
| **Memory** | `21144000` |
| **Topic Tags** | `Linked List, Sorting` |
| **Date** | `2026-09-29 22:17` |

## Solution

```python3
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        current = head
        while current is not None:
            next_node = current.next
            previous = dummy
            while previous.next is not None and previous.next.val < current.val:
                previous = previous.next
            current.next = previous.next
            previous.next = current
            current = next_node
        return dummy.next
```

---
*Generated automatically by [RG Sync](https://github.com).*