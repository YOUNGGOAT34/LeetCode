class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        n=len(grid)
         
        def out_of_bounds(r,c):
            if r<0 or c<0 or r==n or c==n: return True

            
            return False

        land_size=defaultdict(int)
        
        def flip_zeros(r,c):
            visited=set()
            res=1
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if out_of_bounds(nr,nc) or grid[nr][nc]==0:
                    continue

                island_label=grid[nr][nc]
                if island_label not in visited:
                    res+=land_size[island_label]
                    visited.add(island_label)

            return res

       

        def dfs(r,c,label):
            if out_of_bounds(r,c) or grid[r][c]!=1:
                return 0

            size=1
            grid[r][c]=label

            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                size+=dfs(nr,nc,label)

            return size

        

        label=2

        
        for r in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    land_size[label]=dfs(r,c,label)
                    label+=1


        res=0 if not land_size else max(land_size.values())

        for r in range(n):
            for c in range(n):
                if grid[r][c]==0:
                    res=max(res,flip_zeros(r,c))

        return res