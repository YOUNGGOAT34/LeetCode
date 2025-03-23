class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # OR sets a bit
        # XOR unsets a bit
        l=0 #left pointer
        
        curr=0 #current set bits
        res=0

        for r in range(len(nums)):

            while nums[r]&curr:
                curr^=nums[l]
                l+=1
       
            res=max(res,r-l+1)
            curr|=nums[r]

        return res
        