class MinStack:

    def __init__(self):
        self.stack = [[]]
        self.mini = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append([val, self.mini])
        if val< self.mini:
            self.mini = val
        

    def pop(self) -> None:

        x = self.stack.pop()
        self.mini = x[1]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.mini
        
