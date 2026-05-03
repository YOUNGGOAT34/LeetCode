class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m*k>len(bloomDay):
            return -1
        
        def canMakeBouquets(day:int)->bool:

            count=0
            bouquets=0

            for d in bloomDay:

                if d<=day:
                    count+=1
                else:
                    count=0

                if count==k:
                    bouquets+=1
                    count=0

            return bouquets>=m

        left,right=min(bloomDay),max(bloomDay)

        while left<right:
            mid=left+(right-left)//2

            if canMakeBouquets(mid):
                right=mid
            else:
                left=mid+1
        return left

                