"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_intervals = [(i.start,i.end) for i in sorted(intervals, key=lambda x:x.start)]
        max_num_rooms = 0
        heap = []
        """
        15 20

        40 0
        10 5
        """
        for interval in sorted_intervals:
            while heap and heap[0][0] <= interval[0]:
                heapq.heappop(heap)
                print('pop')
            heapq.heappush(heap, (interval[1], interval[0]))
            max_num_rooms = max(max_num_rooms, len(heap))
        return max_num_rooms
            


