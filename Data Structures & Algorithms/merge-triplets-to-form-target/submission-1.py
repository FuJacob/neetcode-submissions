class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets_set = set([tuple(t) for t in triplets])
        for i in range(3):
            for triplet in list(triplets_set):
                if triplet[i] > target[i]:
                    triplets_set.remove(triplet)
        final = []
        for i in range(3):
            vals = [t[i] for t in triplets_set]
            if vals:
                final.append(max(vals))
        
        return target == final



