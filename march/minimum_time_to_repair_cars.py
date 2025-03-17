import math
from typing import List


class Solution:
    def canAssign(self, ranks: List[int], mid: int, cars: int) -> bool:
        count = 0
        for rank in ranks:
            count += math.isqrt(mid // rank)
        return count >= cars

    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 1  
        high = min(ranks) * cars * cars
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            if self.canAssign(ranks, mid, cars):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

        