class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def lowerBound(arr)->int:
            left,right=0,len(arr)

            while left<right:
                mid=(left+right)//2

                if arr[mid]<target:
                    left=mid+1
                else:
                    right=mid

            return left

        def upperBound(arr)->int:
            left,right=0,len(arr)

            while left<right:
                mid=(left+right)//2

                if arr[mid]<=target:
                    left=mid+1
                else:
                    right=mid

            return left

        lb=lowerBound(nums)
        ub=upperBound(nums)-1


        if lb==len(nums) or nums[lb]!=target:
            return [-1,-1] 

        return [lb,ub]






