class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m,n=len(matrix),len(matrix[0])

        left,right=0,(m*n)-1

        while left<=right:
            mid=(right+left)//2

            row,col=mid//n,mid%n

            element=matrix[row][col]

            if element==target:
                return True
            elif element<target:
                left=mid+1
            else:
                right=mid-1

        return False
        