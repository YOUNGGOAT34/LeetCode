from heapq import heapify
import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)

        ops=0

        while nums[0]<k:
            x,y=heapq.heappop(nums),heapq.heappop(nums)
            ops+=1

            heapq.heappush(nums,(x*2+y))


        return ops
        