class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count=defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product=nums[i]*nums[j]

                product_count[product]+=1

        res=0

        for count in product_count.values():
            pairs=(count*(count-1))//2
            res +=8*pairs

        return res
        