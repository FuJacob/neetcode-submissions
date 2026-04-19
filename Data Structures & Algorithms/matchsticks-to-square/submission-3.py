class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0 and n < 4:
            return False
        side_length = total // 4
        sides = [0] * 4
        matchsticks.sort(key=lambda x:-x)
        ans = False
        def backtrack(idx):
            nonlocal ans
            if idx == n:
                if sides == [side_length] * 4:
                    ans = True
                return
            for j in range(4):
                if sides[j] + matchsticks[idx] <= side_length:
                    sides[j] += matchsticks[idx]
                    backtrack(idx+1)
                    sides[j] -= matchsticks[idx]
        backtrack(0)
        return ans




        