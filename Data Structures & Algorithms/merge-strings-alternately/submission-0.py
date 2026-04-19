class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1 = ptr2 = 0
        ans = ''
        count = 0
        while ptr1 < len(word1) or ptr2 < len(word2):
            if ptr2 >= len(word2):
                ans += word1[ptr1:]
                break
            if ptr1 >= len(word1):
                ans += word2[ptr2:]
                break
            if count % 2 == 0:
                ans += word1[ptr1]
                ptr1+=1
            else:
                ans += word2[ptr2]
                ptr2+=1
            count+=1
        return ans




