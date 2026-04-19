class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        char_to_last_idx = {}
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i] not in char_to_last_idx:
                char_to_last_idx[s[i]] = i
        
        end_of_window = 0
        count = 0
        for i in range(n):
            end_of_window = max(end_of_window, char_to_last_idx[s[i]])
            count+=1
            if i == end_of_window:
                ans.append(count)
                count = 0
        return ans
