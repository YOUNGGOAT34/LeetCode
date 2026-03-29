class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        count=0

 

        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a

        n=gcd(a,b)

        for i in range(1,int(sqrt(n))+1):
            if n%i==0:
                count+=1

                if i!=n//i:
                    count+=1

        return count 
        