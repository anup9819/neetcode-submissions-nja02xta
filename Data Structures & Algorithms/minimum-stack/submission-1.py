from collections import deque
class MinStack:

    def __init__(self):
        self.container = deque()
        

    def push(self, val: int) -> None:
        return self.container.append(val)
        
        

    def pop(self) -> None:
        return self.container.pop()
        

    def top(self) -> int:
        return self.container[-1]
        

    def getMin(self) -> int:
        my_deque=self.container
        return min(my_deque)

        
