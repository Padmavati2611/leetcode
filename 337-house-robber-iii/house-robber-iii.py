class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            rob_node = node.val + left[1] + right[1]

            skip_node = max(left) + max(right)

            return (rob_node, skip_node)

        return max(dfs(root))