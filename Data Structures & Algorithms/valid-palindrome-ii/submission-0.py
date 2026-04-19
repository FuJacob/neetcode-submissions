class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            if not s:
                return False
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        l,r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return is_palindrome(s[l+1:r+1]) or is_palindrome(s[l:r])
            l+=1
            r-=1
        return True

