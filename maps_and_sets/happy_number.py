class Solution:
    def isHappy(self, n: int) -> bool:

        seen=set()

        def getDigitSum(n)->int:

            Sum=0
            while n:
                digit=n%10
                
                Sum+=(digit*digit)
                

                n//=10
              

            return Sum

        while n not in seen:
                
                if n==1:
                    return True

                seen.add(n)
                n=getDigitSum(n)

        return False


        

        