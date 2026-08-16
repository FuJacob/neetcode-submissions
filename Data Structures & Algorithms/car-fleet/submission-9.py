class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_speed = list(sorted(zip(position,speed), reverse=True))
        stack = [] ## incresing time 
        for p,s in pos_and_speed:
            time_to_arrival = (target - p) / s
            if not stack or stack[-1] < time_to_arrival:
                stack.append(time_to_arrival)
            
        return len(stack)
                
