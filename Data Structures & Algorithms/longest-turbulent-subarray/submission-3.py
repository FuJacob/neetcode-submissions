class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        ## small represnts longest poss chain, ending at i, where i is SMALL
        small = [1] * n
        big = [1] * n
        ans = [1] * n
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                ans[i] = small[i-1] + 1
                big[i] = ans[i]
            elif arr[i] < arr[i-1]:
                ans[i] = big[i-1] + 1               
                small[i] = ans[i]

        return max(ans)