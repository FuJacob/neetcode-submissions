class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                top = stack.pop()
                result[top[1]] = idx - top[1]
            stack.append((t,idx))
        return result





        