class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        char_to_last_idx = {} ## char to last idx
        n = len(s) ## greddily thats the farhtes we shoud extend
        for i in range(n-1,-1,-1):
            if s[i] not in char_to_last_idx:
                char_to_last_idx[s[i]] = i ## grab last idx
        
        end_of_window = 0 ## end of window
        count = 0 ## how many in our window
        for i in range(n): ## go thru
            end_of_window = max(end_of_window, char_to_last_idx[s[i]]) ## end of window is here,
            count+=1 ## inc count cz we hjsut got another char
            if i == end_of_window: ## if we are at the end of the window, then we split off
                ans.append(count)
                count = 0 ## reset count
        return ans
