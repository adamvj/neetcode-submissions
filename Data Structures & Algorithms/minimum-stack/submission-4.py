class MinStack:

    def __init__(self):
        self.stack = []
        self.min_Stack = []
        return None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_Stack:
            current_min = self.min_Stack[-1]
        else:
            current_min = val
        current_min = min(current_min, val)
        if current_min == val:
            self.min_Stack.append(val)

    def pop(self) -> None:
        num = self.stack.pop()
        if self.min_Stack:
            if num == self.min_Stack[-1]:
                self.min_Stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_Stack:
            return self.min_Stack[-1]
