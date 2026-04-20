class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat[0])
        m=len(mat)

        left,right=0,n-1

        while left<=right:
            mid=(left+right)//2

            maxRow=0

            #find the max element in the mid column

            for i in range(m):

                currentElement=mat[i][mid]

                if currentElement>mat[maxRow][mid]:
                    maxRow=i

            leftNeighbour=mat[maxRow][mid-1] if mid-1>=0 else -1
            rightNeighbour=mat[maxRow][mid+1] if mid+1<n else -1

            if leftNeighbour< mat[maxRow][mid] and rightNeighbour<mat[maxRow][mid]:
                return [maxRow,mid]

            elif leftNeighbour>mat[maxRow][mid]:
                right=mid-1
            else:
                left=mid+1

            
                