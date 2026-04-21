class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        count=0
        
        for i in range(len(grid)):

            left,right=0,len(grid[0])

            while left<right:

                mid=(left+right)//2

                element=grid[i][mid]

                if element<0:
                    right=mid
                else:
                    left=mid+1

            count+=(len(grid[0])-left)

        return count