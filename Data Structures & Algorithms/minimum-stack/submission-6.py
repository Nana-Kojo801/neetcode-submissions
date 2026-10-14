class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = float('inf')
        self.min_values = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_values and val <= self.min_values[-1] or len(self.min_values) == 0:
            self.min_values.append(val)

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.getMin():
            self.min_values.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
