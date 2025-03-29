from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        #find the majority element using moore's algorithm

        majorityElement=nums[0]
        majorityElementFrequency=1
        N=len(nums)

       
        for i in range(1,N):
            if nums[i]==majorityElement:
                majorityElementFrequency+=1
            else:
                
                majorityElementFrequency-=1
                if not majorityElementFrequency:
                    majorityElement=nums[i]
                    majorityElementFrequency+=1

        

        majorityElementFrequency=nums.count(majorityElement)

        


        # find the minimum split index
        res=0
        majorityElementPrefix=0
        for i in range(N-1):
            if nums[i]==majorityElement:
                majorityElementPrefix+=1
                majorityElementFrequency-=1
            if (majorityElementPrefix>(i+1)//2) and (majorityElementFrequency>(N-i-1)//2):
                return i


        return -1
            


        

        