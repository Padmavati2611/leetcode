class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.has_peeked = False
        self.peeked_value = None

    def peek(self):
        if not self.has_peeked:
            self.peeked_value = self.iterator.next()
            self.has_peeked = True
        return self.peeked_value

    def next(self):
        if self.has_peeked:
            value = self.peeked_value
            self.has_peeked = False
            self.peeked_value = None
            return value
        return self.iterator.next()

    def hasNext(self):
        return self.has_peeked or self.iterator.hasNext()