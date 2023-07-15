# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next

        if length == 1:
            return None

        mid_idx = length // 2

        mid = head
        prev = None
        idx = 0
        while idx < mid_idx:
            prev = mid
            mid = mid.next
            idx += 1

        prev.next = mid.next

        return head

    # Fast and Slow Pointers
    def deleteMiddle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None

        slow, fast = head, head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head
