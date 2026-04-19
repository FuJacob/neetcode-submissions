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
   we arent asked ot schedule meetings
   we just want ot find how many overlap at hte same time
   answer = maximum # of concurrent meetings happening at any instant..
   seperate start and end times, since oeralsp onyl change qhen meeting starts or ends..

   starts ends
   sort both
   use 2 pointers
   max_romos 
   rooms = cur meetings
   if new meeting starts before eaerleist end,
   rooms ++1
   otehrwise if newmeeting starts after earleist end
    - meeting ends, increment end poitner
        """
        if not intervals:
            return 0
        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]
        starts.sort()
        ends.sort()
        i = j = 0
        n = len(intervals)
        max_rooms = 0
        rooms_in_use = 0
        while i < n:
            if starts[i] < ends[j]:
                rooms_in_use+=1
                max_rooms = max(max_rooms, rooms_in_use)
                i+=1
            else:
                rooms_in_use-=1
                j+=1 ## move end, since. the next start is afterwards this one curr ends
        return max_rooms

