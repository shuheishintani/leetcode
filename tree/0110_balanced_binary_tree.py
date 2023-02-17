from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # top-down recursion
    # - time: O(NlogN)
    # - space: O(N)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        if not root:
            return True

        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)

        return abs(left_depth - right_depth) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    # bottom-up recursion
    # - time: O(N)
    # - space: O(N)
    def isBalanced2(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
