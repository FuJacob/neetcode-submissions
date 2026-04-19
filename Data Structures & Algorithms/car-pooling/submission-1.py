class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_heap = []
        curr_cap = 0
        trips.sort(key=lambda x:x[1])
        for num, _from, to in trips:
            if not min_heap:
                heapq.heappush(min_heap, (to, num))
                curr_cap = num
            else:
                while min_heap and min_heap[0][0] <= _from:
                    curr_cap -= heapq.heappop(min_heap)[1]
                curr_cap += num
                heapq.heappush(min_heap, (to, num))
            
            if curr_cap > capacity:
                return False
        return True



        