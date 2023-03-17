# def maxDepth2(self, root: Optional[TreeNode]) -> int:
#     if not root:
#         return 0
#
#     level = 0
#     q = deque([root])
#     while q:
#         for i in range(len(q)):
#             node = q.popleft()
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         level += 1
#     return level
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        sum_list = []
        q = deque([root])
        while q:
            row_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                row_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            sum_list.append(row_sum)

        sum_list.sort(reverse=True)

        if k > len(sum_list):
            return - 1

        return sum_list[k - 1]
