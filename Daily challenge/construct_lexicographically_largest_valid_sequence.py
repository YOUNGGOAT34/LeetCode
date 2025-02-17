from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res=[0]*(n*2-1)

        sett=set() # to track the numbers that have already been used
        def backtrack(i):
            if i==len(res):
                return True

            for num in reversed(range(1,n+1)):
                # index validation
                if num in sett:
                    continue

                if num>1 and (i+num>=len(res) or res[i+num]):
                    continue

                #Try a decison

                sett.add(num)
                
                res[i]=num

                if num>1:
                    
                    res[i+num]=num

                # Fill the other positions recursively
                j=i+1

                while j<len(res) and res[j]:
                    j=j+1

                if backtrack(j):
                    return True

                # undo the decision made earlier ,,backtrack

                sett.remove(num)
                
                res[i]=0

                if num>1:
                    
                    res[i+num]=0



            return False

                
            

            

        backtrack(0)

        return res
          