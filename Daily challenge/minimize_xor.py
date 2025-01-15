class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count_bits(n):
            res=0
            while n>0:
                res+=n&1
                n=n>>1

            return res

        count1,count2=count_bits(num1),count_bits(num2)
        x=num1
        i=0
        while count1>count2:

            if x&(1<<i):
                count1-=1

                x=x^(1<<i)

            i+=1


        while count1<count2:

            if x&(1<<i)==0:
                count1+=1

                x=x|(1<<i)

            i+=1


        return x


