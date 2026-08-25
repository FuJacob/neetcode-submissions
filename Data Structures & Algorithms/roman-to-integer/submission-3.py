class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        sym_to_val = {
        'I': 1,
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000, 
        } 
        n = len(s)
        for i in range(n-1,-1,-1):
            curr = sym_to_val[s[i]]
            if i < n - 1 and sym_to_val[s[i+1]] > curr:
                ans -= curr
            else:
                ans += curr
        return ans

            

