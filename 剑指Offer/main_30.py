class MinStack:

    def __init__(self):
        self.container = []
        self.stack = []

    def push(self, x: int) -> None:
        self.container.append(x)
        if len(self.stack) == 0 or self.stack[-1] > x:
            self.stack.append(x)
        else:
            self.stack.append(self.stack[-1])

    def pop(self) -> None:
        self.container.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.container[-1]

    def min(self) -> int:
        return self.stack[-1]
