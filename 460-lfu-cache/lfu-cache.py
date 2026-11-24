from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0

        # key -> value
        self.values = {}

        # key -> frequency
        self.freq = {}

        # frequency -> keys ordered by recent usage
        self.freq_keys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1

        value = self.values[key]
        self._increase_frequency(key)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # Update existing key
        if key in self.values:
            self.values[key] = value
            self._increase_frequency(key)
            return

        # Remove LFU key if cache is full
        if len(self.values) >= self.capacity:
            key_to_remove, _ = self.freq_keys[self.min_freq].popitem(
                last=False
            )

            del self.values[key_to_remove]
            del self.freq[key_to_remove]

        # Add new key with frequency 1
        self.values[key] = value
        self.freq[key] = 1
        self.freq_keys[1][key] = None

        self.min_freq = 1

    def _increase_frequency(self, key: int) -> None:
        old_freq = self.freq[key]

        # Remove key from its old frequency group
        del self.freq_keys[old_freq][key]

        # If this was the last key at minimum frequency,
        # increase the minimum frequency
        if old_freq == self.min_freq:
            if not self.freq_keys[old_freq]:
                self.min_freq += 1

        # Increase frequency
        new_freq = old_freq + 1
        self.freq[key] = new_freq

        # Add key to the end (most recently used)
        self.freq_keys[new_freq][key] = None