class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_speed = list(zip(position,speed))
        pos_and_speed.sort(reverse=True)
        def get_time(target, p, s):
            return (target - p) / s
        stack = [] ## incresing time 
        for p,s in pos_and_speed:
            time_to_arrival = get_time(target,p,s)
            if not stack or stack[-1] < time_to_arrival:
                stack.append(time_to_arrival)
            
        return len(stack)
                
