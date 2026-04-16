class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=float('inf')
        nums.sort()

        for i in range(len(nums)):

            left,right=i+1,len(nums)-1

            while left<right:
                total=nums[i]+nums[left]+nums[right]

                ans=total if abs(total-target)<abs(ans-target) else ans

                if total>target:
                    right-=1

                else:
                    left+=1

        return ans