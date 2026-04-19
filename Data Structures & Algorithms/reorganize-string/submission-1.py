class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = [(-count,char) for char,count in freq.items()]
        heapq.heapify(heap)
        last = None
        ans = ""
        while heap:
            count,char = heapq.heappop(heap) 
            ans += char
            if last: 
                heapq.heappush(heap, last)
            if count+1 == 0:
                last = None
            else:
                last = (count+1, char)
        return ans if not last else ""