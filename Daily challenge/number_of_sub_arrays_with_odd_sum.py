from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        curr_sum=0# current sum
        odd_freq=0 # the odd sums encountered so far
        even_freq=0 # even sums encountered so far
        res=0
        MOD=10**9+7

        for n in arr:
            curr_sum+=n
            if curr_sum&1:
                res=(res+even_freq+1)%MOD
                odd_freq+=1

            else:
                res=(res+odd_freq)%MOD
                even_freq+=1

        return res

        