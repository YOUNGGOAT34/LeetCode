class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        max_sum=window_sum

        for right in range(k,len(nums)):
            window_sum+=nums[right]
            window_sum-=nums[right-k]

            max_sum=max(window_sum,max_sum)

        return max_sum/k