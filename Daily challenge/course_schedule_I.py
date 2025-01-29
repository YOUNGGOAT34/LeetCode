class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pqMap={i:[] for i in range(numCourses)}
        visited=set()

        for crs,pq in prerequisites:
            pqMap[crs].append(pq)

        def dfs(crs):
            if crs in visited:
                return False

            if not pqMap[crs]:
                return True
            visited.add(crs)
            for pq in pqMap[crs]:
                if not dfs(pq):
                    return False

            visited.remove(crs)
            pqMap[crs]=[]
            return True

        for pq in pqMap:
            if not dfs(pq): return False

        return True

        