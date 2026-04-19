"""
jhashjset wihtout bukt un ahs tagle lbiraries

imlpement my hashset class

add
contains
remove

cant use any bult in hash tble lbiraries.
huh..


okay how woudl i make this then 
how do we do a quick contains check ?
 o 1

o1 hm ? 
good question.

were gona design hash set
[ [] [] [] ]
buckets
were gonna essientally
o1 on average sma buckets


hash function too
n

"""
class MyHashSet:

    def __init__(self):
        self.N = 1000
        self.buckets = [[] for _ in range(self.N)]

    def _hash(self,key):
        return key % self.N

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.buckets[self._hash(key)].append(key)
        

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return

        hashed_key = self._hash(key)
        for i in range(len(self.buckets[hashed_key])):
            if self.buckets[hashed_key][i] == key:
                self.buckets[hashed_key].pop(i)
    
    def contains(self, key: int) -> bool:
        hashed_key = self._hash(key)
        for i in range(len(self.buckets[hashed_key])):
            if self.buckets[hashed_key][i] == key:
                return True
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)