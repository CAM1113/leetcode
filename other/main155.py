class MinStack:

    def __init__(self):
        self.container = []
        self.min = 1e5

    def push(self, x: int) -> None:
        self.container.append(x)
        if x < self.min:
            self.min = x

    def pop(self) -> None:
        x = self.top()
        self.container.pop()
        if x == self.min:
            self.min = self.set_min()

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        return self.min

    def set_min(self):
        if len(self.container) == 0:
            return
        self.min = self.container[0]
        for i in self.container:
            if i < self.min:
                self.min = i
