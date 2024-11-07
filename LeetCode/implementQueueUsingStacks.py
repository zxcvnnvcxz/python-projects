class MyQueue:

    def __init__(self):
        self.list = []

    def push(self, x: int) -> None:
        self.list.insert(0, x)

    def pop(self) -> int:
        self.temp = self.list[-1]
        self.list.pop(-1)
        return self.temp

    def peek(self) -> int:
        return self.list[0]

    def empty(self) -> bool:
        if not self.list:
            return True
        else:
            return all(isinstance(sli, list) and self.empty() for sli in self.list)

if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()