from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xIntervals=[(coordinate[0],coordinate[2]) for coordinate in rectangles]
        yIntervals=[(coordinate[1],coordinate[3]) for coordinate in rectangles]

        #sort the intervals
        xIntervals.sort()
        yIntervals.sort()

        #helper function to count number of non-overlapping intervals
        def nonOverlappingIntervals(intervals:List[int])->int:
            count=0
            previousEndInterval=-1

            for startInterval,endInterval in intervals:
                if startInterval>=previousEndInterval: 
                    #means their is no overlapping
                    count+=1
                previousEndInterval=max(endInterval,previousEndInterval)

            return count

        # nonOverlappingIntervals(xIntervals)  -->for vertical cuts
        #nonOverlappingIntervals(yIntervals) --> for horizontal cuts

        return max(nonOverlappingIntervals(xIntervals),nonOverlappingIntervals(yIntervals))>=3
        