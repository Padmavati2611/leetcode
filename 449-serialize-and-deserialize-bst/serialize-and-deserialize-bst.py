from collections import deque

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values = data.split(",")

        root = TreeNode(int(values[0]))
        queue = deque([root])

        index = 1

        while queue:
            node = queue.popleft()

            if index < len(values) and values[index] != "null":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)

            index += 1

            if index < len(values) and values[index] != "null":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)

            index += 1

        return root