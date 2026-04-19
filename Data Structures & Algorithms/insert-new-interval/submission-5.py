class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        intervals
        sroted ascending

        new interval start end
        insert new interval into intervals s.t. its still sorted in ascending and no overlapping interals
        merge if needed

        well let's find the very first interval that has start before our start
        """
        ans = []
        i = 0
        n = len(intervals)
        ## find the start of the thingy so then we can merge
        ## add all intervalds that end before newinterval
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i+=1
        

        start,end = newInterval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        ## this merges all overlapping
        ans.append([start,end])

        while i < n:
            ans.append(intervals[i])
            i+=1
        return ans




        