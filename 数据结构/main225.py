class MyStack:

    def __init__(self):
        self.l = []

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> int:
        return self.l.pop()

    def top(self) -> int:
        return self.l[-1]

    def empty(self) -> bool:
        return len(self.l) == 0
