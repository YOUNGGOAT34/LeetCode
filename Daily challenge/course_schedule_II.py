class Solution:
    def findOrder(self, numCourses: int, pqs: List[List[int]]) -> List[int]:
        pqMap={i:[] for i in range(numCourses)} # pqMap-prerequisite map

        for crs,pq in pqs:
            pqMap[crs].append(pq)

        visited=set() #means we have already included it in the output
        visiting=set() #for cycle detection

        res=[]

        def dfs(crs):
            if crs in visiting: # there is a cycle
                return False

            if crs in visited: #it is already processed
                return True
            visiting.add(crs) # add it to the current path
            for pq in pqMap[crs]: # get all its neighbors
                if not dfs(pq): return False
            visiting.remove(crs) # remove it from the path cause we are done
            visited.add(crs)
            res.append(crs)

            return True

        for crs in pqMap:
            if not dfs(crs): # this means there was a cycle hence we need to return an empty array
               return []

        return res

            

           

        for crs in pqMap:
            if not dfs(crs): return []

        return res

        