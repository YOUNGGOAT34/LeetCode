class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        number_of_flips=0
        max_len=0
        left=0

        for i in range(len(nums)):

            if nums[i]==0:
                number_of_flips+=1

            while number_of_flips>k:
                if nums[left]==0:
                    number_of_flips-=1

                left+=1

            max_len=max(max_len,i-left+1)

        return max_len

 

            

            