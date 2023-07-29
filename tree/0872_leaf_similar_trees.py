# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def count_leaf_recursive(root: TreeNode, res: List[int]):
            if not root.left and not root.right:
                res.append(root.val)

            if root.left:
                count_leaf_recursive(root.left, res)

            if root.right:
                count_leaf_recursive(root.right, res)

        res1, res2 = [], []

        count_leaf_recursive(root1, res1)
        count_leaf_recursive(root2, res2)

        return res1 == res2

    # Using generator
    def leafSimilar2(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))
