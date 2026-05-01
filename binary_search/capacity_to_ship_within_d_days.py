class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
     

        def canShip(capacity:int)->int:

            currentWeight=0
            numberOfDays=1
            for weight in weights:
                if currentWeight+weight>capacity:
                    numberOfDays+=1
                    currentWeight=0

                currentWeight+=weight
                   
            return numberOfDays


        left,right=max(weights),sum(weights)

        while left<right:
            capacity=left+(right-left)//2

            daysUsed=canShip(capacity)

            if daysUsed<=days:
                right=capacity
            else:
                left=capacity+1

        return left

            