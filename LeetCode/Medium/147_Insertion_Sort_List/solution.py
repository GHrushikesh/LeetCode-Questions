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