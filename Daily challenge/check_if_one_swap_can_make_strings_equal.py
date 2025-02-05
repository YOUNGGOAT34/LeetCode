class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        indices=[]

        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                indices.append(i)

            if len(indices)>2:
                return False

            

        if len(indices)==2:
            i,j=indices
            return s1[i]==s2[j] and s1[j]==s2[i]

        return len(indices)==0
        