class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        direction={
            1:[0,1],
            2:[0,-1],
            3:[1,0],
            4:[-1,0]
        }

        
        ROWS,COLS=len(grid),len(grid[0])

        q=deque([(0,0,0)]) #r,c,cost
        min_cost={(0,0):0}

        while q:
            r,c,cost=q.popleft()
            
            if (r,c)==(ROWS-1,COLS-1):
                return cost

            for d in direction:
                d_row,d_col=direction[d] #direction row and direction column
                
                n_row,n_col=r+d_row,c+d_col # get the new row and new column
                n_cost=cost if d==grid[r][c] else cost + 1 

                if (n_row<0 or n_col<0 or
                    n_row==ROWS or n_col==COLS or
                    n_cost>=min_cost.get((n_row,n_col),float("inf"))
                
                ):
                   continue

                min_cost[(n_row,n_col)]=n_cost



                if d==grid[r][c]:
                    q.appendleft((n_row,n_col,cost))

                else:
                    q.append((n_row,n_col,cost+1))




         