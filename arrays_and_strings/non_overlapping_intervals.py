class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        k=0

        previousEnd=intervals[0][1]

        for start,end in intervals[1:]:
            if start<previousEnd:
                k+=1
            else:
                previousEnd=end
           
        return k

                    
                        
                        
                    

        