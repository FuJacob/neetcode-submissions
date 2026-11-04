"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_rooms = 0
        intervals.sort(key=lambda x: (x.start,x.end))
        heap = []
        for i in intervals: 
            while heap and heap[0] <= i.start:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)
            min_rooms = max(min_rooms, len(heap))
        return min_rooms