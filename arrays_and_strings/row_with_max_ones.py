class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index=0
        no_of_ones=0


        for i in range(len(mat)):
           
            ones=sum(mat[i])
            if ones>no_of_ones:
                no_of_ones=ones
                index=i
          
                

        return [index,no_of_ones]