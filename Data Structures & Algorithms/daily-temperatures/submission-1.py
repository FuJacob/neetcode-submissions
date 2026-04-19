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

        for idx, temp in enumerate(temperatures):
            for i in range(idx, len(temperatures)):
                if temp < temperatures[i]:
                    result[idx] = i - idx
                    break
        return result

