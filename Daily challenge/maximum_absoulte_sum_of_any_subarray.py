from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=0
        min_sum=0

        curr_max_sum=0
        curr_min_sum=0

        # fin the maximum sum

        for n in nums:
            curr_max_sum+=n
            curr_min_sum+=n
            max_sum=max(max_sum,curr_max_sum)
            min_sum=min(min_sum,curr_min_sum)
            if curr_max_sum<0:
                curr_max_sum=0

            if curr_min_sum>0:
                curr_min_sum=0

        

        return max(max_sum,abs(min_sum))
        