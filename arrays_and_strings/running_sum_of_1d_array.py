class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=0
        ans=[0]*len(nums)

        for i in range(len(nums)):
            prefix+=nums[i]
            ans[i]=prefix

        return ans
