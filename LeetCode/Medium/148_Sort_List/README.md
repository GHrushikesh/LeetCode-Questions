# #148 - 148. Sort List

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `162` |
| **Memory** | `40532000` |
| **Topic Tags** | `Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort` |
| **Date** | `2026-09-29 22:15` |

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        dummy = ListNode(0)
        current = dummy
        while left is not None and right is not None:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        if left is not None:
            current.next = left
        else:
            current.next = right
        return dummy.next
```

---
*Generated automatically by [RG Sync](https://github.com).*