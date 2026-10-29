class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        values = []

        def preorder(node):
            if not node:
                values.append("N")
                return

            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(values)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        values = iter(data.split(","))

        def build():
            val = next(values)

            if val == "N":
                return None

            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()