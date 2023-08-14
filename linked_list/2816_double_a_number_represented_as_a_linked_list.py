# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class ListNode:
    pass


class Solution:
    # Not accepted by the error when converting large number to string
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        str_num = str(head.val)
        while head.next:
            str_num += str(head.next.val)
            head = head.next

        doubled = str(int(str_num) * 2)

        nodes = []
        for str_d in doubled:
            nodes.append(ListNode(int(str_d)))

        if len(nodes) == 0:
            return None

        res_head = nodes[0]
        cur = res_head
        for i in range(1, len(nodes)):
            cur.next = nodes[i]
            cur = cur.next

        return res_head

    def doubleIt2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        while head:
            num = num * 10 + head.val
            head = head.next
        num *= 2

        dummy = ListNode()
        cur = dummy

        digits = []
        if num == 0:
            digits = [0]
        while num > 0:
            digits.append(num % 10)
            num //= 10

        for digit in reversed(digits):
            cur.next = ListNode(digit)
            cur = cur.next

        return dummy.next
