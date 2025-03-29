from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums=[r for row in grid for r in row]
        nums.sort()

        for row in grid:
            for number in row:
                if number%x !=grid[0][0]%x:
                    return -1
          
        
        mid=len(nums)//2
        res=0
        for n in nums:
            gapBetween=abs(nums[mid]-n)
            res+=(gapBetween)//x

        return res
