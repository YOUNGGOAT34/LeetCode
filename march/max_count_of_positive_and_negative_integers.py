from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def leftBisect():
            high=len(nums)-1
            low=0

            while low<high:
                mid=(high+low)//2
                if nums[mid]<0:
                    low=mid+1
                else:
                    high=mid


            return low


        def rightBisect():
            high=len(nums)-1
            low=0

            while low<high:
                mid=(high+low)//2
                if nums[mid]<=0:
                    low=mid+1
                else:
                    high=mid

            return low



        return max(leftBisect(),len(nums)-rightBisect())
        