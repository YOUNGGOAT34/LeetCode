class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canFinish(k:int)->int:
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/k)

            return hours

        left,right=1,max(piles)

        while left<right:
            k=left+(right-left)//2

            hours=canFinish(k)

            if hours<=h:
                right=k
            else:
                left=k+1

        return left

            
        
