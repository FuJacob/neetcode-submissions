"""
given MyHashMap

void put key value
inserts key value

pair 

key already exists? 
udpate corespdongi value 

need ot do a hash map wiht key value

get should be ocnsntat

wait jamybe we can do aame thing as a hash set right?
does has gurantee uniqueness? 
"""
class MyHashMap:

    def __init__(self):
        self.N = 100
        self.buckets = [[] for _ in range(self.N)]
    
    def _hash(self, key):
        return key % self.N
    
    def put(self, key: int, value: int) -> None:
        h_key = self._hash(key)
        bucket = self.buckets[h_key]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i][1] = value
                return
        bucket.append([key,value])

        
    def get(self, key: int) -> int:
        h_key = self._hash(key)
        bucket = self.buckets[h_key]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]
        return -1
        
    def remove(self, key: int) -> None:
        h_key = self._hash(key)
        bucket = self.buckets[h_key]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)