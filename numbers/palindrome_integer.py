class Solution:
    def isPalindrome(self, x: int) -> bool:

        
        if x<0 and (x%10==0 and x!=0):
            return False

        reversedX=0
        n=x

        while n>0:
            lastDigit=n%10
            reversedX=(reversedX*10)+lastDigit
            n//=10

        return reversedX==x
        