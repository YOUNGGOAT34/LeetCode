from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq_map={} # count the frequency of i-nums[i] to note that we have ssen it before hence we can make a good pair/pairs
        N=len(nums)
        good_pairs=0
        total_pairs=(N*(N-1))//2

        for i in range(N):
            if i-nums[i] in freq_map:
                good_pairs+=freq_map[i-nums[i]]
                freq_map[i-nums[i]]+=1

            else :
                freq_map[i-nums[i]]=1

            


        return total_pairs-good_pairs


        