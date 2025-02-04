class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        N=len(nums)

        res=nums[0]
        curr=nums[0]

        for i in range(1,N):
            if nums[i-1]<nums[i]:
                curr+=nums[i]
            else:
                curr=nums[i]

            res=max(curr,res)

        return res
                
        