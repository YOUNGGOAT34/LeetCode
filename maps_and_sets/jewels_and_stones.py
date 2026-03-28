class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewelSet=set(jewels)

        count=0

        for stone in stones:
            if stone in jewelSet:
                count+=1

        return count
        