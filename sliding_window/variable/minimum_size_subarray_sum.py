class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_length=float('inf')
        window_sum=0
        left=0

        for i in range(len(nums)):
            window_sum+=nums[i]

            while window_sum>=target:
                window_sum-=nums[left]
                min_length=min(min_length,i-left+1)
                left+=1


        return 0 if min_length==float('inf') else min_length

