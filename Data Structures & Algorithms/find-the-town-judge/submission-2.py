class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ## 1 indedxed right
        out = [0] * (n+1)
        _in = [0] * (n+1)
        for a,b in trust:
            out[a] +=1
            _in[b] +=1
        for idx, (o,i) in enumerate(zip(out,_in)):
            if idx != 0 and o == 0 and i == n-1:
                return idx
        return -1   
