"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_concurrent_rooms = 0
        intervals.sort(key=lambda x:x.start)
        heap = []
        for interval in intervals:
            start,end = interval.start, interval.end
            while heap and heap[0][0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, (end, start))
            max_concurrent_rooms = max(max_concurrent_rooms, len(heap))
        return max_concurrent_rooms
        