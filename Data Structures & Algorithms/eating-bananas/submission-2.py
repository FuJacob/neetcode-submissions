class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        ## we want the first True
        l, r = 1, max(piles)
        def get_time_eat(piles, k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return time

        while l < r:
            m = l + (r-l) // 2
            if get_time_eat(piles,m) <= h: ## we can eat. at this time or faster, lets try smalelr
                r = m
            else: ## otherwise we arent 
                l = m + 1
        return l ## l is the answer once we only have one 

