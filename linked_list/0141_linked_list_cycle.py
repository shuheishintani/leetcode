# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # cycle finding algorithm
    # - time: O(N)
    # - space: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while slow != fast and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow == fast
