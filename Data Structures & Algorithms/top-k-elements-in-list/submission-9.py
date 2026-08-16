class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] +=1
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        for v, f in freq.items():
            buckets[f].append(v)
        ans = []
        for i in range(n, -1,-1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans
                

