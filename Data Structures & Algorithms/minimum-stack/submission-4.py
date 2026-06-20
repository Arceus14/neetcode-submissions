class MinStack:

    def __init__(self):
        self.mini = 2**32 - 1
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.mini = min(self.mini, val)
        self.min_stack.append(self.mini)
        self.stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        if len(self.min_stack) > 1:
            self.mini = self.min_stack[-1]
        elif len(self.min_stack) == 1:
            self.mini = 2**31 - 1
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
