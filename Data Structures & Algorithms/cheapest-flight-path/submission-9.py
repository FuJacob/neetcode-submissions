class Solution:
    """
    1. track all shortest airpot to time
    2. build adj graph so u can see whre u can go
    3. start with airport to time for source = 0
    4. move across neighbors, keep track of stpos, i guess lvl. k times
    no cycles. directed? 
    no fligths from airpot to titself.
    cycles? if so , keep visited.
    5. relax dostanes as u figorue ot thefasest tim e to oget to a node
    """
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        airport_to_cost = [float('inf')] * n
        airport_to_cost[src] = 0
        ## how many stops we want? 
        ## only k so we iterate k+ 1 times then right?
        ## only k times
        for i in range(k+1):
            tmp = airport_to_cost[:]
            for f,t,p in flights:
                ## < tmp, our current one so far 
                if airport_to_cost[f] + p < tmp[t]:
                    tmp[t] = airport_to_cost[f] + p
            airport_to_cost = tmp
        return airport_to_cost[dst] if airport_to_cost[dst] != float('inf') else -1

                    
