"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        curr = min_rooms = 0
        events = []
        for i in intervals:
            events.append((i.start, 1))
            events.append((i.end, -1))
        events.sort()
        for _, delta in events:
            curr += delta
            min_rooms = max(curr, min_rooms)
        return min_rooms
