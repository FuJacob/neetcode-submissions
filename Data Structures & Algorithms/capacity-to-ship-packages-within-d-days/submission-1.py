class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo,hi = max(weights), sum(weights)
        def all_shipped(capacity): ## returns whether cam ship al lwithin capacity within days
            count = 1
            curr = 0
            for weight in weights:
                if curr + weight > capacity:
                    curr = weight
                    count+=1
                else:
                    curr += weight
            return count <= days
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if all_shipped(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo




            