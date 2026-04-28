import math
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber != 0:
            last_digit = columnNumber % 26
            if last_digit == 0:
                ans.append('Z')
            else:
                new_digit = last_digit + ord('A') - 1
                ans.append(chr(new_digit))
            columnNumber -=1
            columnNumber //= 26
        return "".join(list(reversed(ans)))

