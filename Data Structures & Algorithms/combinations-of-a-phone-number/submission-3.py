class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {'2': 'abc', '3': 'def','4': 'ghi', '5': 'jkl','6': 'mno', '7': 'pqrs','8': 'tuv', '9': 'wxyz' 
        }
        ans = []
        curr = []
        n = len(digits)
        if not digits:
            return []
        def backtrack(start):
            if len(curr) == n:
                ans.append("".join(curr))
                return

            for i in range(len(digit_to_letters[digits[start]])):
                curr.append(digit_to_letters[digits[start]][i])
                backtrack(start+1)
                curr.pop()
        backtrack(0)
        return ans