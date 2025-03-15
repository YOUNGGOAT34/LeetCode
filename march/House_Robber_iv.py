from typing import List


class Solution:
    #BS
    def minCapability(self, nums: List[int], k: int) -> int:

        def isCapable(mid:int)->bool:
            i=0
            count=0

            while i<len(nums):
                if nums[i]<=mid:
                    i+=2
                    count+=1
                else:
                    i+=1
                if count==k:
                    break
            return count==k


        low,high=min(nums),max(nums)
        res=0
        while low<=high:
            mid=low+(high-low)//2

            if isCapable(mid):
                res=mid
                high=mid-1

            else:
                low=mid+1

        return res
        