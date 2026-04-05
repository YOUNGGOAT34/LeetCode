class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        seen=defaultdict(int)
        max_sum=0
        window_sum=0

      
        
        for i in range(k):
            seen[nums[i]]+=1
            window_sum+=nums[i]
            
            

        if len(seen)==k:
            max_sum=window_sum
        

        for right in range(k,len(nums)):
            seen[nums[right-k]]-=1
            window_sum-=nums[right-k]
            window_sum+=nums[right]
            
            if seen[nums[right-k]]==0:
                del seen[nums[right-k]]
            seen[nums[right]]+=1
            if len(seen)==k:
                max_sum=max(max_sum,window_sum)


        return max_sum




