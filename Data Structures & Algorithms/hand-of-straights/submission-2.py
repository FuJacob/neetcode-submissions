class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        val_to_count = Counter(hand)
        ## gredily we use the smalest numbers to be the start right?
        ## yeah greedily pick the smallest #s to be the start
        ## check do we have at least one copy x...x+groupSize - 1?  for eahc
        ## if not , return False
        ## if all exist, decrement counts
        while val_to_count:
            start = min(val_to_count.keys())
            for i in range(groupSize):
                if start+i in val_to_count:
                    val_to_count[start+i] -=1
                    if val_to_count[start+i] == 0:
                        del val_to_count[start+i]
                else:
                    return False
        return True

