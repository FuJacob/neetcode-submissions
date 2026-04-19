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
            
        while i < n and intervals[i][0] < newInterval[0]:
            ans.append(intervals[i])
            i+=1
        
        j = i-1
        for interval in [newInterval] + intervals[j+1:]:
            if ans and ans[-1][1] >= interval[0]:
                start,end = ans.pop()
                ans.append([start, max(interval[1], end)])
            else:
                ans.append(interval)

        return ans




        