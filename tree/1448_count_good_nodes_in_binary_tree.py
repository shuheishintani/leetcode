# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, parentMax: int) -> int:
            if not root:
                return 0

            if root.val >= parentMax:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, parentMax) + dfs(root.right, parentMax)

        return dfs(root, -10 ** 4 - 1)
