class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            max_sum = max(max_sum, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return max_sum