class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for idx in range(n):
            while stack and temperatures[idx] > temperatures[stack[-1]]:
                top = stack.pop()
                result[top] = idx - top
            stack.append(idx)
        return result





        