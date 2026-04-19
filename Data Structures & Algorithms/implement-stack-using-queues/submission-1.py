
class MyStack:

    def __init__(self):
        self.q1 = deque([]) 
        self.q2 = deque([])
        self.ptr = self.q1 ## which ever queue we are to look at
        self.ptr2 = self.q2

    def push(self, x: int) -> None:
        self.ptr.append(x)
    
    def pop(self) -> int:
        while len(self.ptr) > 1:
            self.ptr2.append(self.ptr.popleft())
        ans = self.ptr.popleft()
        self.ptr, self.ptr2 = self.ptr2, self.ptr
        return ans
        
    def top(self) -> int:
        while len(self.ptr) > 1:
            self.ptr2.append(self.ptr.popleft())
        ans = self.ptr[0]
        self.ptr2.append(self.ptr.popleft())
        self.ptr, self.ptr2 = self.ptr2, self.ptr
        return ans

        

    def empty(self) -> bool:
        return not self.ptr
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()