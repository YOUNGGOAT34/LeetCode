class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans=[]



        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1

        while top<=bottom and left<=right:

            #Go right

            for col in range(left,right+1):
                ans.append(matrix[top][col])
            top+=1

            #Go down

            for row in range(top,bottom+1):
                ans.append(matrix[row][right])

            right-=1

            #Go left
            if top<=bottom:

                for col in range(right,left-1,-1):
                    ans.append(matrix[bottom][col])

                bottom-=1

            #Go up

            if left<=right:

    
                for row in range(bottom,top-1,-1):
                    ans.append(matrix[row][left])

                left+=1


        return ans


        