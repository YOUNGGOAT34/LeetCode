class NumArray:

    prefixSum=[]

    def __init__(self, nums: List[int]):
        self.prefixSum=[0]*len(nums)

        prefix=0

        for i in range(len(nums)):
            prefix+=nums[i]
            self.prefixSum[i]=prefix

        

        
    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.prefixSum[right]
        return self.prefixSum[right]-self.prefixSum[left-1]



        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

