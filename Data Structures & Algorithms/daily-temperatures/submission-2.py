class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        you're given array of integers temperatures where temperatures[i]
        represents the daily temperatures on the ith day


        we want to return an array result where result[i] is the number of days 
        after the ith day before a warmer temperatjre appears
        if there is not day in the future, set to 0
        okay
        naive way
        """
        result = [0] * len(temperatures)
        stack = []

        ## essientally we will keep waiting list of days that need their next warmerest day
        ## that way we only iterate trhoughg one pass, and by doing one pass we end up 
        ## being able to sovle for multiple days.

        for today, temp_today in enumerate(temperatures):
            ## while stack still has elements and while our today's temp si bigger than the top of our 
            ## stack
            while stack and temp_today > temperatures[stack[-1]]:
                ## append answer for that day, pop it off
                waiting_day = stack.pop()
                result[waiting_day] = today - waiting_day
            ## then what we need to do is add our day
            stack.append(today)

        return result
