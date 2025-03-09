class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        greater=[]
        pivots=[]

        for i in range(len(nums)):
            if nums[i]<pivot:
                less.append(nums[i])

            elif nums[i]>pivot:
                greater.append(nums[i])

            else:
                pivots.append(nums[i])
                


        return less+pivots+greater
        