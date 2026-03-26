class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows=len(matrix)
        columns=len(matrix[0])

        #Transpose

        for i in range(rows):
            for j in range(i+1,columns):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        #reverse the columns

        for i in range(columns):
            left=0
            right=len(matrix[0])-1

            while left<=right:
                matrix[i][left],matrix[i][right]=matrix[i][right],matrix[i][left]
                left+=1
                right-=1


        

        