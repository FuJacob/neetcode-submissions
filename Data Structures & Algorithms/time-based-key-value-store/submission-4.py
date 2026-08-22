class TimeMap:

    def __init__(self):
        self.key_to_timestamps = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_timestamps[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        ## timestamp_prev <= timestmap
        ## very largest one
        ## ie the very last TRUE. <=? l = m 
        ## else r = m - 1 too high 
        timestamps = self.key_to_timestamps[key]
        l, r = 0, len(timestamps) - 1
        
        ans = ""
        while l <= r:
            m = l + (r-l)//2
            if timestamps[m][0] <= timestamp:
                ans = timestamps[m][1]
                l = m + 1
            else:
                r = m - 1
        return ans
        
