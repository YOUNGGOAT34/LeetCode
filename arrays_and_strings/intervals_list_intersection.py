class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        res=[]
        
        if not firstList or not secondList:
            return res

        n=len(firstList)
        N=len(secondList)

        i=0
        j=0

        while i<n and j<N:
            start=max(firstList[i][0],secondList[j][0])
            end=min(firstList[i][1],secondList[j][1])

            if start<=end:
                res.append([start,end])

            if firstList[i][1]<secondList[j][1]:
                i+=1

            else:
                j+=1


        return res


