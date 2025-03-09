class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def prime_number():
            is_prime=[True]*(right+1)
            is_prime[0]=is_prime[1]=False

            for i in range(2,int(sqrt(right))+1):
                if not is_prime[i]:
                    continue
                for j in range(i+i,right+1,i):
                    is_prime[j]=False

            primes=[]
            for i in range(len(is_prime)):
                if is_prime[i] and i>=left:
                    primes.append(i)

            return primes

        prime_numbers=prime_number()
        res=[-1,-1]
        difference=float("inf")

        for i in range(1,len(prime_numbers)):
            if prime_numbers[i]-prime_numbers[i-1]<difference:
                difference=prime_numbers[i]-prime_numbers[i-1]
                res=[prime_numbers[i-1],prime_numbers[i]]

        return res
