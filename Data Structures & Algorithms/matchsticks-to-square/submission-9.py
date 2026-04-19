class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0 or n < 4:
            return False
        side_length = total // 4
        sides = [0] * 4
        matchsticks.sort(key=lambda x:-x)
        def backtrack(idx):
            if idx == n:
                return True

            for j in range(4):
                if sides[j] + matchsticks[idx] <= side_length:
                    sides[j] += matchsticks[idx]
                    if backtrack(idx+1):
                        return True
                    sides[j] -= matchsticks[idx]
                if sides[j] == 0:
                    break
            return False
        return backtrack(0)




        