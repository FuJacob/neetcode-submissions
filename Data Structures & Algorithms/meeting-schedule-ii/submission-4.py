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
        given meetingtime aintervla objects
        consisitning of start and end times 
        find minimum # of days requid to schedle all meetinsg no conflicts

At any moment in time, how many meetings are happening concurrently

max # of meetinsg tha hpapen oncucnrrlty cuz  thats what elas the # of days we really need

2
starts        0 5 15
ends        40 10 20

start
min heap for end itmes, we look for the one that ends the fastest 
minimize concucrrnet
process thru startends, when adding meeting oging on rn, add its end time
then when on next start, check if we start afetr the end time if not, then add it 

if it works then we pop the smallest cuz thats same day then

o n
increment 
        """
        concurrent = 0
        min_days = 0
        ongoing_end_times = []
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if ongoing_end_times:
                earliest_end = ongoing_end_times[0]
                if earliest_end <= interval.start:
                    heapq.heappop(ongoing_end_times)
                else:
                    concurrent +=1
                heapq.heappush(ongoing_end_times, interval.end)
            else:
                concurrent +=1
                ## add it here too 
                heapq.heappush(ongoing_end_times, interval.end)
            min_days = max(min_days, concurrent)
        return min_days












