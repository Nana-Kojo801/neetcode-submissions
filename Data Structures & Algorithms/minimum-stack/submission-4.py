class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = float('inf')
        self.min_values = []

    def push(self, val: int) -> None:
        #[-2, -2, -3, -3]
        self.stack.append(val)
        if not self.min_values:
            self.min_values.append(val)
        else:
            if val <= self.min_values[-1]:
                self.min_values.append(val)
    """
    min_value = -3
    # [-2, -2, -3, -3]
    """
    def pop(self) -> None:
        val = self.stack.pop()
        if self.getMin() == val:
            self.min_values.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]