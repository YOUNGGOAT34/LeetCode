class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged=[]

        for i in range(len(intervals)):

            if intervals[i][0]>newInterval[1]:
                merged.append(newInterval)
                return merged+intervals[i:]

            elif intervals[i][1]<newInterval[0]:
                merged.append(intervals[i])

            else:
                newInterval=[min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]

        merged.append(newInterval)
  

        return merged
        