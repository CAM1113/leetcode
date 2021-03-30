class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                return -1
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()

