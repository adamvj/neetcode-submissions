class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        return None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            current_min = self.min_stack[-1]
        else:
            current_min = val
        current_min = min(current_min, val)
        if current_min == val:
            self.min_stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.min_stack:
            if popped == self.min_stack[-1]:
                self.min_stack.remove(popped)

    def top(self) -> int:
        top_of_stack = self.stack[-1]
        return top_of_stack
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
