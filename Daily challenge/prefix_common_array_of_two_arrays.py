class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(B)

        setA,setB=set(),set()

        result=[0]*n

        for i in range(n):
            result[i]=result[i-1]
            if A[i]==B[i]:
                result[i]+=1

            else:
                if A[i] in setB:
                    result[i]+=1

                if B[i] in setA:
                    result[i]+=1

            setA.add(A[i])
            setB.add(B[i])

        return result