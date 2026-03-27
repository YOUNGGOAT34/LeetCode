class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m=len(board)
        n=len(board[0])
        
        def helper(r,c):
            neighbors=[[-1,-1],
                 [-1,1],
                 [-1,0],
                 [0,-1],
                 [0,1],
                 [1,-1],
                 [1,1],
                 [1,0]
            
            ]

            count=0

            for row,col in neighbors:
                if (row+r>=0 and r+row<m) and (c+col>=0 and c+col<n):
                    if board[row+r][col+c]>0:
                        
                        count+=1

            return count


        for row in range(m):
            for col in range(n):
                neighbours=helper(row,col)
                if board[row][col]:
                    if neighbours>3:
                        board[row][col]=2

                    elif neighbours in [2,3]:
                        board[row][col]=3
                    elif neighbours<2:
                        board[row][col]=2

                else:
                    if neighbours==3:
                        board[row][col]=-1


        for row in range(m):
            for col in range(n):
                if board[row][col]:
                    
                    if board[row][col]==2:
                        board[row][col]=0
                    elif board[row][col]==3:
                        board[row][col]=1

                    elif board[row][col]==-1:
                        board[row][col]=1





