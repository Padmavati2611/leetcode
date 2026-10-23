class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not inorder or not postorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])

        return root