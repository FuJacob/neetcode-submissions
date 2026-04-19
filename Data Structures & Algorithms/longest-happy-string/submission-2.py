class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ""
        heap = []
        for pair in [(-a, 'a'),(-b, 'b'),(-c, 'c')]:
            if pair[0] != 0:
                heapq.heappush(heap, pair)
        while heap:
            count, char = heapq.heappop(heap)
            if len(ans) >= 2 and ans[-2:] == char * 2: 
                if not heap:
                    return ans

                new_count,new_char = heapq.heappop(heap)
                ans += new_char
                new_count +=1
                if new_count != 0:
                    heapq.heappush(heap, (new_count, new_char))
            else:
                ans += char
                count+=1
            if count != 0:
                heapq.heappush(heap, (count, char))
        return ans




