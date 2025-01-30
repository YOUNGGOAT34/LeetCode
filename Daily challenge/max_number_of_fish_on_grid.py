class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        visited=set()
        def dfs(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visited or grid[r][c]==0:
                return 0

           

            visited.add((r,c))
            res=grid[r][c]
            neighbors=[[r+1,c],[r-1,c],[r,c-1],[r,c+1]]

            for n_row,n_col in neighbors:
                res+=dfs(n_row,n_col)

            return res

            

            




        res=float('-inf')

        
        

        for r in range(ROWS):
            for c in range(COLS):
                
                    res=max(dfs(r,c),res)
        return res


        