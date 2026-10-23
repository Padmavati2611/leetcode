class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result