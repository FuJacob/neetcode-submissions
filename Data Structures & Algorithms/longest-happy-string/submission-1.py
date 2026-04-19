class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ""
        heap = []
        if a != 0:
            heapq.heappush(heap,(-a,'a'))
        if b != 0:
            heapq.heappush(heap,(-b,'b'))
        if c != 0:
            heapq.heappush(heap,(-c,'c'))
        
        while heap:
            count, char = heapq.heappop(heap)
            if len(ans) >= 2 and ans[-2:] == char * 2: 
                if not heap:
                    return ans
                new_count,new_char = heapq.heappop(heap)
                ans += new_char
                new_count +=1
                if new_count != 0:
                    heapq.heappush(heap, (new_count, new_char)) ## use second most count
            else:
                ans += char
                count+=1
            if count != 0:
                heapq.heappush(heap, (count, char))
        return ans




