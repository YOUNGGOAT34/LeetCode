class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minElement=min(nums)
        maxElement=max(nums)

        while minElement:
            maxElement,minElement=minElement,maxElement%minElement

        return maxElement