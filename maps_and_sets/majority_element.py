class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans=None
        count=0
        for num in nums:
            if count==0:
                ans=num
            if num==ans:
                count+=1
            else:
                count-=1
                
            
        return ans

    
        