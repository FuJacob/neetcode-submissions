"""
we want an algorithm that oclelcts daily price qutes for stock and return sspan of the stocks price
for curr day
span of a stocks price in 1 day si the max # of consecutive days 
fo which the stock price was LESS THAN or equla to the price of that day

max num

monotonic stack
we keep a stack thats always eequal or decreasing than teh top of the stack
if it isnt, we keep popping tikl it is
use global coutner to keep track of most ? noon ly car about cur
rso tis jsut the curr # of stocks on it 
"""
class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:        
        self.stack.append(price)
        tmp = 0
        idx = len(self.stack) - 1
        while idx >= 0 and price >= self.stack[idx]:
            tmp+=1
            idx-=1
        return tmp
        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)