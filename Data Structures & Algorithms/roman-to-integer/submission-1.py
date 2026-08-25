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
        ptr = n - 1
        while ptr >= 0:
            ans += sym_to_val[s[ptr]]
            curr = s[ptr]
            ptr -=1
            if ptr >= 0:
                nxt = s[ptr]
                if nxt == 'I' and (curr == 'V' or curr == 'X'):
                    ans -= sym_to_val[nxt]
                    ptr -= 1
                if nxt == 'X' and (curr == 'L' or curr == 'C'):
                    ans -= sym_to_val[nxt]
                    ptr -= 1
                if nxt == 'C' and (curr == 'D' or curr == 'M'):
                    ans -= sym_to_val[nxt]
                    ptr -= 1
        return ans

            

