class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        heap = [(0,k)]
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((t,v))
        while heap:
            curr_dist, node = heapq.heappop(heap)
            if curr_dist > dist[node]:
                continue
            for nxt_t,nxt_node in graph[node]:
                new_dist = nxt_t + curr_dist

                if new_dist < dist[nxt_node]:
                    dist[nxt_node] = new_dist
                    heapq.heappush(heap, (dist[nxt_node], nxt_node))
        min_time = max(dist[1:])
        if min_time == float('inf'):
            return -1
        return min_time

        
