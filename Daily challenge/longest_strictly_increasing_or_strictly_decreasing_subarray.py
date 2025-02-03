class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        result=1
        current=1
        increasing=False

        for i in range(1,n):
            if nums[i-1]<nums[i]:
                if increasing:
                    current+=1
                else:
                    current=2
                    increasing=True

            elif nums[i-1]>nums[i]:
                if not increasing:
                    current+=1
                else:
                    current=2
                    increasing=False
            else:
                current=1
                increasing=False

            result=max(result,current)

        return result
            

        
        