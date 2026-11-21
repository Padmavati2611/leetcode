class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                for child in node.children:
                    queue.append(child)

            result.append(level)

        return result