class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N=len(grid[0])
        topRowSum,bottomRowSum=grid[0],grid[1]

        for i in range(1,N):
            topRowSum[i]+=topRowSum[i-1]
            bottomRowSum[i]+=bottomRowSum[i-1]

        res=float ("inf")

        for i in range(N):
            topRow=topRowSum[-1]-topRowSum[i] #points that second robot can take on the top row
            bottomRow=bottomRowSum[i-1] if i>0 else 0 #points the second robot can take from the bottom row

            secondRobotPoints=max(topRow,bottomRow) #Find the maximum between the top row and the bottom

            res=min(res,secondRobotPoints)


        return res






