class Stack:
    stack = []
    
    def __init__(self, size: int) -> None:
        self.size = size
        self.topi: int = 0
        self.stack = [-1] * (self.size + 1)
        print(self.stack)

    def top(self) -> any:
        return self.stack[self.topi]

    def empty(self) -> bool:
        if self.topi == 0:
            return True
        else:
            return False
        
    def push(self, element: any) -> None:
        if self.topi == self.size:
            print("Stack overflow")
        else:
            self.topi += 1
            self.stack[self.topi] = element

    def pop(self) -> any:
        if self.empty():
            print("Stack underflow")
        else: 
            self.topi -= 1
            return self.stack[self.topi + 1]
    
    def __str__(self) -> str:
        return self.stack.__str__
