from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        previousEnd=0
        meetings.sort()
        for startInterval,endInterval in meetings:
            startInterval=max(startInterval,previousEnd+1)
            daysMeetingTook=endInterval-startInterval+1 # +1 because the start and end intervals are inclusive
            previousEnd=max(previousEnd,endInterval)

            days-=max(daysMeetingTook,0) #incase the days become 0

        return days

        