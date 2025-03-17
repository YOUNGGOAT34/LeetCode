from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        oddCount=set()

        for num in nums:
            if num not in oddCount:
                oddCount.add(num)

            else:
                oddCount.remove(num)

        return len(oddCount)==0

        