class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        current = head

        while current:
            if current.child:
                next_node = current.next
                child_node = current.child

                current.next = child_node
                child_node.prev = current
                current.child = None

                tail = child_node
                while tail.next:
                    tail = tail.next

                if next_node:
                    tail.next = next_node
                    next_node.prev = tail

            current = current.next

        return head