class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        
        n=len(s)



        j=0

        for i in range(len(t)):
            if j<n and s[j]==t[i]:
                j+=1

        return j==n

        
        

        

        
        