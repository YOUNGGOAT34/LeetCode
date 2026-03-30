class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter=defaultdict(int)
      

        if len(s)!=len(t):
            return False

        for c in s:
            counter[c]+=1

        for c in t:
            counter[c]-=1
            if counter[c]<0:

                return False

        return True