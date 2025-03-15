from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canAssign(mid:int)->bool:
            count=0

            for pile in candies:
                if pile>=mid:

                
                  count+=pile//mid

            return count>=k

        low=1
        high=max(candies)
        res=0

        while low<=high:
            mid=low+(high-low)//2

            if canAssign(mid):
                res=max(res,mid)
                low=mid+1
            else:
                high=mid-1

        return res


        