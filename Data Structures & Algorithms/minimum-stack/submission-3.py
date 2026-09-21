class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        self.cur_min=float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.cur_min > val:
            self.cur_min = val
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.cur_min)


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

        self.cur_min=self.min_stack[-1] if len(self.min_stack) >0 else float('inf')

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
