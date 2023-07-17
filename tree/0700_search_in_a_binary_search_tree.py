# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursion
    # Time complexity: O(H), O(logN) in the average case, O(N) in the worst case
    # Space complexity: O(H) to keep the recursion stack
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        while True:
            if root.val > val:
                return self.searchBST(root.left, val)
            elif root.val < val:
                return self.searchBST(root.right, val)
            else:
                return root

    # Iterative
    # Time complexity: O(H)
    # Space complexity: O(1)
    def searchBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root
