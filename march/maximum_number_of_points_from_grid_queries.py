from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], q: List[int]) -> List[int]:
        ROWS,COLS=len(grid),len(grid[0])

        queries=[(number,index) for index,number in enumerate(q)]
        queries.sort()
        minHeap=[]
        heappush(minHeap,(grid[0][0],0,0))
        res=[0]*len(queries)
        points=0
        visited=set([(0,0)])

        for number,index in queries:
            while minHeap and minHeap[0][0]<number:
                value,r,c=heappop(minHeap)

                points+=1

                neighbors=[[r+1,c],[r-1,c],[r,c-1],[r,c+1]]

                for nr,nc in neighbors:
                    if (nr,nc) not in visited and 0<=nr<ROWS and 0<=nc<COLS:
                        visited.add((nr,nc))
                        heappush(minHeap,(grid[nr][nc],nr,nc))


            res[index]=points

        
        return res
        