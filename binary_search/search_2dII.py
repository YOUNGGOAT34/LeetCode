class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=0,len(matrix[0])-1

        while col>=0 and row<len(matrix):
            element=matrix[row][col]

            if element==target:
                return True

            elif element<target:
                row+=1
            else:
                col-=1

        return False
