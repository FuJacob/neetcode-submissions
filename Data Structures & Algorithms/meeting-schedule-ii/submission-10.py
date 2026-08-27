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
        intervals.sort(key=lambda x:x.start)
        ans = 0
        time_to_delta = defaultdict(int)
        for interval in intervals:
            time_to_delta[interval.start] += 1
            time_to_delta[interval.end] -= 1
        curr = 0
        events = sorted(time_to_delta.items())
        for _, change in events:
            curr += change
            ans = max(curr, ans)
        
        return ans


        

