class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        given n gas stations
        2 integer arrays:
        - gas: gas[i] represents amount of gas at ith station
        - cost: cost[i] is the amount of gas needed to travel from ith station to i+1th station (last station is conencted ot first station)

        car that can store an unlimited amount of gas

you begin the journey with an empty tank at one of the gas stations

starting gas station's index such that you can travel around the circuit once in the clockwise direction
 gas = [1,2,3,4], 
 cost = [2,2,4,1]

greedy problem:
- make tjhe most optiaml local choice to ge tthe global optimal

only one soltunio


return -1

optiamlly we start wit hthe msot gas and try ot move around
not the least gas
cuz then we waste right

whether we cna even posbsile to travel once in clockwise dirceiotn or not
[1,2,3,4,1,2,3,4], cost = [2,2,4,1,2,2,4,1]
curr_gas = 4
num_stations = 1
n-1 times we want to travel, ie touch n gas stations


the best start point is the station right after the point of minimumzed gas, maximuzed cost 
        """
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        cur_gas = 0
        start_idx = 0 
        for i, (g,c) in enumerate(zip(gas,cost)):
            cur_gas += g
            cur_gas -= c
            if cur_gas < 0:
                start_idx = i+1 ## has to be after
                cur_gas = 0 ## erstart cur gas? 
        return start_idx