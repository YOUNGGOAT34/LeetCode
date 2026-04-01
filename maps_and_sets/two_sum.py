class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen={}

        #for each value in the array ,how much do you need to reach the target>??
        for i,num in enumerate(nums):
            needed=target-num

            if needed in seen:
                return [i,seen[needed]]

            seen[num]=i
            
       

 
        