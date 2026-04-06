class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p)>len(s):
            return []
        
        sCount=defaultdict(int)
        pCount=defaultdict(int)

        for i in range(len(p)):
            pCount[p[i]]+=1
            sCount[s[i]]+=1

        res=[0] if pCount==sCount else []

        for i in range(len(p),len(s)):
            sCount[s[i-len(p)]]-=1
            if sCount[s[i-len(p)]]==0:
                del sCount[s[i-len(p)]]

            sCount[s[i]]+=1

            if sCount==pCount:
                res.append(i-len(p)+1)

        return res

            
