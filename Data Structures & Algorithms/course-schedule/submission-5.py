class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_courses = defaultdict(list)
        ## course to courses represents u ened to take course to take the crouses
        indegree = [0] * numCourses
        for a,b in prerequisites:
            course_to_courses[b].append(a)
            indegree[a] +=1
        roots = [course for course, indeg in enumerate(indegree) if indeg == 0]
        q = deque(roots)
        visited = set(roots)
        ## check if cycle, if cycle then return FAlse?
        while q:
            course = q.popleft() ## we jsut finsied
            for nei in course_to_courses[course]:
                if nei not in visited:
                    indegree[nei] -=1
                    if indegree[nei] == 0:
                        visited.add(nei)
                        q.append(nei)
        return len(visited) == numCourses



