class Solution:
    def tribonacci(self, n: int) -> int:
        prev0 = 0
        prev1 = 1
        prev2 = 1
        for _ in range(n):
            tmp = prev2
            prev2 += prev1 + prev0
            prev0 = prev1
            prev1 = tmp
        return prev0

        