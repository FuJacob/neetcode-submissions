"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [x.start for x in sorted(intervals, key=lambda x:x.start)]
        ends = [x.end for x in sorted(intervals, key=lambda x:x.end)]
        rooms_in_use = 0
        max_rooms = 0
        n = len(intervals)
        start_ptr = end_ptr = 0
        while start_ptr < n and end_ptr < n:
            start = starts[start_ptr]
            end = ends[end_ptr]
            if start < end:
                rooms_in_use +=1
                start_ptr+=1
            else:
                rooms_in_use -=1
                end_ptr+=1

            max_rooms = max(max_rooms, rooms_in_use)
        return max_rooms