class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        target = total // 2
        dp = [False] * (target+1)
        dp[0] = True
        ## wdym? 
        ## its 0 1 kanspack, if we iterat htru the shit we use, backwards, then it wil work
        ## then iterate thur all teh shit values
        ## this way ,we onyl ever use eahc one once
        for stone in stones:
            for i in range(target,stone-1,-1):
                if dp[i-stone]:
                    dp[i] = True
        
        for i in range(target, -1,-1):
            if dp[i]:
                return total - 2 * i
        return 0


