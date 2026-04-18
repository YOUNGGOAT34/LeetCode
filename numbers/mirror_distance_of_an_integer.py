class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverseN=0

        x=n

        while x>0:

            lastDigit=x%10
            reverseN=(reverseN*10)+lastDigit
            x//=10

        return abs(reverseN-n)
    