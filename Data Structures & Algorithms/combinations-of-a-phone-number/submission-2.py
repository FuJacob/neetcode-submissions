class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        _map = {"2":["a","b","c"],"3":["d","e","f"],
        "4":["g","h","i"],"5":["j","k","l"],
        "6":["m","n","o"],"7":["p", "q","r","s"],
        "8":["t","u","v"],"9":["w","x","y","z"]}

        ans = []
        curr = []
        if not digits: return []
        def backtrack(start):
            ## base case
            if start == len(digits):
                ans.append("".join(curr))
                return
            ## iterate thru poss options
            options = _map[digits[start]]
            for char in options:
                curr.append(char)
                backtrack(start+1)
                curr.pop()
        backtrack(0)
        return ans

