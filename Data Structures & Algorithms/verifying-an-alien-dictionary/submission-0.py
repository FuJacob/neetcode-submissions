class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_to_ord = {}
        for i, o in enumerate(order):
            letter_to_ord[o] = i
        for i in range(1, len(words)):
            n,m = len(words[i]), len(words[i-1])
            ptr1, ptr2 = 0,0
            good = False
            while ptr1 < m or ptr2 < n: ## check
                if ptr1 == m:
                    break
                if ptr2 == n:
                    return False
                diff = letter_to_ord[words[i][ptr2]] - letter_to_ord[words[i-1][ptr1]]
                if diff > 0:
                    break
                elif diff < 0:
                    return False
                ptr1+=1
                ptr2+=1
        return True
