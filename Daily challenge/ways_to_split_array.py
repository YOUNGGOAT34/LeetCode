class Solution(object):
    def waysToSplitArray(self, nums):
        right=sum(nums)
        left=0
        result=0

        for i in range(len(nums)-1):
            left+=nums[i]
            right-=nums[i]

            result+=1 if left>=right else 0

        return result

        