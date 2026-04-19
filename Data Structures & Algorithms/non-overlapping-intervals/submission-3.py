class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        minimum # of intervals to remove to make rest of itnervals non overapping

        MIN to remove. well either we reove the one before, or the one after.
        best to remove the one after, so least conflicts
        seems we overcoutned.

        why?
        why we overcount.
        i dont know why.

        i think we overcounted. because why ? 
        why? why? we over counted.
        whjat do i need to fucking do here?
        i dont get it .
        hm? 
        OHH
        no.
        im wrong
        its never better to remove the one after u idiot
        its beteer to remove which ever one is longer end which has bigger chance hurt others
        i assumed always better keep the first one but its actuall the one with longer end that hurts

        """
        intervals.sort()
        count = 0
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] < stack[-1][1]:
                if intervals[i][1] > stack[-1][1]:
                    count +=1
                    continue
                count+=1
                stack.pop()
            stack.append(intervals[i])
        return count
                



