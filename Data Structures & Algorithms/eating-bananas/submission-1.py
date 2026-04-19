class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        you're given integer array piles
        given integer h = number of hours you have to eat all bananas


        you may decide your bananas per hour eating rate of k
        - at each hour, you choose piule of bannas, and eat k banans from that pile.

        if it has less than k, you fnish eating it, but you still cannot eat another in the same hour
        return min integer k s.t. you can eat all bnanas within h hours


        okay so

        well easist is that we eat the highest # of banans in a pile
        find the max, then eat that.
        then since we know that piles.length <= h 100%
        then we're gurantee t ofinsh all the bannas by h hours.

        but we want min.
        so tehcincally we can check all the way from 1 banna per hour. ... -> max banna per hour
        hmm.
        so we can check each one, but if we do, the time complexity of that is o(len(piles) * maxbannas)
        but we could porbaly do even better by doing binary search usign the # of bannas eaten per hour.
        every time it equals or takes less than h hours, we cna do binary seacrh. if it doesn't work. we return the glob
        min we held at that time.


        so then time complexity becomes o(len(piles) * log maxbannas)


        """
        maxPile = max(piles)
        ans = maxPile
        l, r = 1, maxPile - 1
        while l <= r:
            k = l + (r-l)//2
            curr_ans = 0
            for pile in piles:
                ## rounds up by adding k but -1 then floor
                curr_ans += (pile + k - 1) // k
            if curr_ans <= h:
                ans = min(k, ans)
                r = k - 1
            else:
                l = k + 1
        return ans
                


            

