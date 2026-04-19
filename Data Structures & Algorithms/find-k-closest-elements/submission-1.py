class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sum_diff = 0
        ptr = 0
        bounds = None
        best_diff = float('inf')
        n =len(arr)
        for i in range(n):
            sum_diff += abs(x-arr[i])
            while ptr < n and i - ptr + 1 >= k:
                if sum_diff < best_diff:
                    best_diff = sum_diff
                    bounds = (ptr, i)
                sum_diff -= abs(x-arr[ptr])
                ptr+=1
        return arr[bounds[0]:bounds[1]+1]


