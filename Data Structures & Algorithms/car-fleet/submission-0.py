class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        okay n cars tragelling same place on 1 lane
        given:
        array of integers position -> length n
    
        array of integers speed -> length n 
        dest is at posotion target miles


        car cnanot pass another car ahegad of it. can only catch up and drife @ same speed


        car fleet is non empty set of cars driving at the same position and same speed
        a single car is also considered a car fleet
        if car catches up tpo car  fleet the moment fleet reaches desitno the car ispart of the fleet

        retujr # of different car fleets that will arrive at desitnatin


        well we know that we can calculate the. time it will take a car to reach desition
        right
        (target - postion) / speed
        if a car is faster, and ends up there faster, then it would be collide with al lthe other cars slwoer than it in front of it
        that becomes a fleet
        

        4 1 0 7

        """
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        ## times to get to end
        times = [((target-pos) / spd) for pos,spd in cars]
        stack = []
        for t in times:
            if not stack:
                stack.append(t)
            ## if one on stack is slower or equal, then the new t will be part of a fleet
            ##3 continue then since it's considered as poart of tthat fleet
            if stack[-1] >= t:
                continue
            ## otherwise we need to make another fleet
            else:
                stack.append(t)
        ## whatever left on stack is the answer
        return len(stack)



        