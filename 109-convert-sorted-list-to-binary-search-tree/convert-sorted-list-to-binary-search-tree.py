class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        if not head:
            return None

        values = []
        while head:
            values.append(head.val)
            head = head.next

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(values[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(values) - 1)