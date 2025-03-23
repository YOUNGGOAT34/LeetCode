from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def flips(i):
            nums[i]=0 if nums[i] else 1
            
        res=0
        for i in range(len(nums)-2):
            if not nums[i]:
                flips(i)
                flips(i+1)
                flips(i+2)
                res+=1

        if not nums[-1] or not nums[-2]:
            return -1
        return res
        