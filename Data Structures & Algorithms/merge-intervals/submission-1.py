class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= stack[-1][1]:
                start,end = stack.pop()
                stack.append([start, max(end, intervals[i][1])])
            else:
                stack.append(intervals[i])
        return stack
