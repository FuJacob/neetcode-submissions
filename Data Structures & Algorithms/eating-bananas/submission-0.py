class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        given integer array piles
        where piles[i] is the # of banans in the ith pile
        you're also given integer h
        which preresens nu mof hours you have to eat all bannas
        """
        ## we will do binary search
        ## essientally we will need to consider every k 
        ## from 1 to max banans in a pile
        ## since if we pick max bannas pile it will be the entire
        ## 100% guranteed to work as len piles is going to be less tha h 
        ## so we can just do binary ssearch
        ## find max
        _max = max(piles)
        l, r = 1, _max - 1
        _min = _max

        while l <= r:
            ## binary search
            m = l + (r-l)//2
            time = 0
            for pile in piles:
                time += (pile + m - 1) // m
            if time <= h:
                _min = min(_min, m)
                r = m - 1
            else:
                l = m + 1
        return _min
                

