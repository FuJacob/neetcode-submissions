"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        okay we have some intervals
        we need to find the min num of days required to schedule all meetings
        so fi there's an overlap, that's when we know we need to create a new day for it


        """
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res, count = 0,0
        s, e = 0,0
        while s < len(intervals):
            if start[s] < end[e]:
                count+=1
                res = max(res, count)
                s+=1
            else:
                count-=1
                e+=1
        return res



        