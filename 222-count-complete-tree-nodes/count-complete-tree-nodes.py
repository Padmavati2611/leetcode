
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        def get_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        height = get_height(root)

        if height == 1:
            return 1

        left_height = get_height(root.right)

        if left_height == height - 1:
            return (1 << (height - 1)) + self.countNodes(root.right)
        else:
            return (1 << (height - 2)) + self.countNodes(root.left)
