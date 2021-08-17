class MaxQueue:

    def __init__(self):
        self.queue = []
        self.max_stack = []

    def max_value(self) -> int:
        if len(self.max_stack) == 0:
            return -1
        return self.max_stack[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while len(self.max_stack) > 0 and self.max_stack[-1] < value:
            self.max_stack.pop()
        self.max_stack.append(value)

    def pop_front(self) -> int:
        if len(self.queue) == 0:
            return -1
        val = self.queue.pop(0)
        if val == self.max_stack[0]:
            self.max_stack.pop(0)
        return val