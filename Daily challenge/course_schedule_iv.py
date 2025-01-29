class Solution:
    def checkIfPrerequisite(self, numCourses: int, pqs: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj=defaultdict(list)

        for pq,crs in pqs:
            adj[crs].append(pq)

        pqMap={}
        def dfs(crs):
            if crs not in pqMap:
                pqMap[crs]=set()
                for pq in adj[crs]:
                    pqMap[crs]|=dfs(pq)
                pqMap[crs].add(crs)
            return pqMap[crs]
        res=[]

        for crs in range(numCourses):
            if crs not in pqMap:
                dfs(crs)


        for u,v in queries:
            res.append(u in pqMap[v])

        return res

        