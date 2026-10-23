class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        clones = {}

        current = head
        while current:
            clones[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            clones[current].next = clones.get(current.next)
            clones[current].random = clones.get(current.random)
            current = current.next

        return clones[head]