class Solution:
    def mySqrt(self, x: int) -> int:
        
        left,right=1,x

        while left<=right:
            mid=(right+left)//2

            square=mid**2

            if square==x:
                return mid
            elif square<x:
                left=mid+1
            else:
                right=mid-1

        return right