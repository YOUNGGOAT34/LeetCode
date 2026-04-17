class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans=[]
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue

                left,right=j+1,len(nums)-1

                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        ans.append([nums[j],nums[i],nums[left],nums[right]])

                        left+=1
                        right-=1

                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1

                    elif total>target:
                        right-=1

                    else:
                        left+=1
        
        return ans