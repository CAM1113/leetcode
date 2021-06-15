class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.used = []

    def get(self, key: int) -> int:
        if not (key in self.map.keys()):
            return -1
        val = self.map[key]
        self.used.remove(key)
        self.used.insert(0, key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            self.map[key] = value
            self.used.remove(key)
            self.used.insert(0, key)
            return
        self.used.insert(0, key)
        self.map[key] = value
        if self.capacity < len(self.used):
            del self.map[self.used[-1]]
            self.used.pop()