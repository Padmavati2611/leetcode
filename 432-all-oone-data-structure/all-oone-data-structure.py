class AllOne:

    def __init__(self):
        self.count = {}
        self.buckets = {}
        self.min_count = 0
        self.max_count = 0

    def inc(self, key: str) -> None:
        old = self.count.get(key, 0)
        new = old + 1

        self.count[key] = new
        self.buckets.setdefault(new, set()).add(key)

        if old > 0:
            self.buckets[old].remove(key)
            if not self.buckets[old]:
                del self.buckets[old]

        if not self.buckets:
            self.min_count = new
        else:
            self.min_count = min(self.buckets)

        self.max_count = max(self.buckets)

    def dec(self, key: str) -> None:
        old = self.count[key]
        new = old - 1

        self.buckets[old].remove(key)

        if not self.buckets[old]:
            del self.buckets[old]

        if new == 0:
            del self.count[key]
        else:
            self.count[key] = new
            self.buckets.setdefault(new, set()).add(key)

        if self.buckets:
            self.min_count = min(self.buckets)
            self.max_count = max(self.buckets)
        else:
            self.min_count = 0
            self.max_count = 0

    def getMaxKey(self) -> str:
        if not self.buckets:
            return ""
        return next(iter(self.buckets[self.max_count]))

    def getMinKey(self) -> str:
        if not self.buckets:
            return ""
        return next(iter(self.buckets[self.min_count]))