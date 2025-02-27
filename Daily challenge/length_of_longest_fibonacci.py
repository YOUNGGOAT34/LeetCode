from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        sett=set(arr)

        res=0

        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                prev,curr=arr[i],arr[j]
                nxt=curr+prev

                length=2

                while nxt in sett:

                    prev,curr=curr,nxt
                    nxt=curr+prev

                    length+=1

                    res=max(res,length)


        return res

        