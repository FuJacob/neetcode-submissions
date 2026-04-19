class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse=True)
        times = [(target - p)/s for p,s in cars]
        stack = []
        for t in times:
            if not stack:
                stack.append(t)
            elif stack[-1] >= t:
                continue
                ## if the next on stack is slower than the one beforei t, thje nt ibecomes a fleet
            else:
                stack.append(t)
        return len(stack)
                