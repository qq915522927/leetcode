class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)



    def deleteHead(self) -> int:

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        return -1


if __name__ == "__main__":
    q = CQueue()

    print(q.appendTail(3), q.deleteHead(), q.deleteHead(), q.deleteHead())