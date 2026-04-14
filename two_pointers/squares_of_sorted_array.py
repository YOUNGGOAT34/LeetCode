class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n

        pos=n-1

        left=0
        right=n-1

        while left<=right:
            if abs(nums[left])<abs(nums[right]):
                ans[pos]=nums[right]**2
                right-=1
            else:
                ans[pos]=nums[left]**2
                left+=1

            pos-=1

 

        return ans
        