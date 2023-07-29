# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        left = []

        while fast and fast.next:
            left.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        res = 0
        while slow:
            v = left.pop()
            res = max(res, v + slow.val)
            slow = slow.next

        return res
