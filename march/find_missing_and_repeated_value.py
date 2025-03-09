class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)

        hashmap=defaultdict(int)

        res=[0]*2

      

        for i in range(n):
            for j in range(n):
               hashmap[grid[i][j]]+=1


        for num in range(1,n*n+1):
            if hashmap[num]==2:
                res[0]=num

            if  hashmap[num]==0:
                res[1]=num
            


                


        return res

        
        