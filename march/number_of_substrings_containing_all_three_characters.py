from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left=0
        vowelCount=defaultdict(int)
        
        res=0
        for right in range(len(s)):
            vowelCount[s[right]]+=1

            while len(vowelCount)==3:
                res+=(len(s)-right)
                vowelCount[s[left]]-=1
                if vowelCount[s[left]]==0:
                    vowelCount.pop(s[left])
                left+=1

        return res

        