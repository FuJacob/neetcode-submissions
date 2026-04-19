class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        given array of integers stones where stones[i] re[resnets weight of ith stone
        ew want to run a simluatio
        2 heaviest
        heap
        """
        stones = list(map(lambda x:-x, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x == y:
                continue
            if x < y:
                heapq.heappush(stones, -(y - x))
        return -stones[0] if len(stones) > 0 else 0

