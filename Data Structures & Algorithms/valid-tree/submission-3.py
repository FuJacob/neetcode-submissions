class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        node_to_nodes = defaultdict(list)
        for a,b in edges:
            node_to_nodes[a].append(b)
            node_to_nodes[b].append(a) 
        visited = set([0])
        q = deque([0])
        while q:
            node = q.popleft()
            for nei in node_to_nodes[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return len(visited) == n
            
