class MedianFinder:

    def __init__(self):
        self.bigger = [] ## min heap
        self.smaller = [] ## max heap

    def addNum(self, num: int) -> None:
        ## if num is bigger than smallest big, need go to other side.
        ## realance too so neverm ore than 1 difence, this way we mainta niwhat? o(1) find median but addoUi s log n
        if not self.smaller or num > -self.smaller[0]:
            heapq.heappush(self.bigger, num)
        else:
            heapq.heappush(self.smaller, -num)

    def findMedian(self) -> float:
        while abs(len(self.smaller) - len(self.bigger)) > 1:
            if len(self.smaller) > len(self.bigger):
                heapq.heappush(self.bigger, -heapq.heappop(self.smaller))
            else:
                heapq.heappush(self.smaller, -heapq.heappop(self.bigger))
        
        if (len(self.bigger) + len(self.smaller)) % 2 != 0:
            if len(self.bigger) > len(self.smaller):
                return self.bigger[0]
            return -self.smaller[0]
        return (self.bigger[0] - self.smaller[0]) / 2

