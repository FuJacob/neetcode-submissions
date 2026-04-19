class TimeMap:
    """
    we need to implement a time based key value data structure
    that supports
    - storing multiple values for the same key @ specified timestamps
    - retireving the key vlaue @ specified timestamp
    """

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_map.get(key, [])
        ## we need to return most recent value of key
        ## and the most recent timestamp, where timestamp is less than or equal to given timestamp
        if not arr:
            return ""
        l,r = 0, len(arr) - 1
        res = ""
        while l <= r:
            m = (l+r)//2
            ## cases:
            ## if the mid timestamp is bigger than given timestamp, we want to 
            ## to look into the left side of the mid
            ## iof it equals then return
            if arr[m][1] == timestamp:
                return arr[m][0]
            ## if its 
            if arr[m][1] > timestamp:
                r = m - 1
            else:
                ## otherwise it's too small, so how do we know if it's a solution r not
                ## well honestly we could stop binary search when it's kjust 1 element left 
                ## so either iet returns wh'en equal or leaves us the last element that's the cloest
                ## and it wont be bigger because we always check as u can see if it's to big, we resize
                ## so what if it's too small? move it right
                ## well it's a possible answer
                res = arr[m][0]
                l = m +1
        return res

        
