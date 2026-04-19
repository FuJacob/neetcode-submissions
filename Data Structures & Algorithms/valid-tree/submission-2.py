class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        node_to_nodes = defaultdict(list)
        for a,b in edges:
            node_to_nodes[a].append(b) ## this is a graph for only one direction ## we want all its UNDRIRECTED
            node_to_nodes[b].append(a) ## i can go here too
            ## ITS UNDIRECTED
        visited = set([0]) ## we visit
        q = deque([0])
        while q:
            node = q.popleft()
            for nei in node_to_nodes[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return len(visited) == n
            
