class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = sorted(zip(timestamp, username, website))
        username_to_website = defaultdict(list)
        for _,u,w in data:
            username_to_website[u].append(w)
        ## user name to ordered list of website they visited
        pattern_count = defaultdict(int)

        for username, website in username_to_website.items():
            seen = set()
            m = len(website)
            for i in range(m):
                for j in range(i+1, m):
                    for k in range(j+1, m):
                        pattern = (website[i],website[j], website[k]) ##unique per user u dmb fuck
                        seen.add(pattern)
            for pattern in seen:
                pattern_count[pattern] +=1
        
        best_pattern = None
        best_count = 0
        for pattern, count in pattern_count.items():
            if count > best_count:
                best_count = count
                best_pattern = pattern
            elif count == best_count and pattern < best_pattern:
                best_pattern = pattern
            

        return list(best_pattern)
        
        
