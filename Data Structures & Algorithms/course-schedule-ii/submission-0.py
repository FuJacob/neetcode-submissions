class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        preqreusiuistes = a,b
        b -> a


        numcourses
        return valid ordering of courses you fan take to fiish all courses
        topological sort since we need to process children first then parent
        """
        order = []
        indegree = [0] * numCourses
        course_to_courses = defaultdict(list) ## repesntes take course b, what other courses depend on it 
        for a,b in prerequisites:
            course_to_courses[b].append(a)
            indegree[a] +=1
        roots = [i for i,indeg in enumerate(indegree) if indeg == 0]
        q = deque(roots)

        while q:
            course = q.popleft() ## we ifnished this guy
            order.append(course)
            for nei in course_to_courses[course]: 
                indegree[nei] -=1 ## we finshed procesing one of your guys here
                if indegree[nei] == 0: ## if its ready send it over
                    q.append(nei)
        return order if len(order) == numCourses else []





        
