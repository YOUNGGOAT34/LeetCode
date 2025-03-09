class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        #backtracking solution
        # def backtrack(index,curr_sum)->bool:
        #     if curr_sum==n:
        #         return True

        #     if curr_sum>n or 3**index>n:
        #         return False

        #     #2 decisions :include it or skip it
        #     if backtrack(index+1,curr_sum+3**index):
        #         return True

        #     return backtrack(index+1,curr_sum)

        index=0

        while 3**index<=n:
            index+=1

        index-=1 # because it goes beyond by one for the above loop to become false

        while index>=0:
            power=3**index
            if power<=n:
                n-=power
            index-=1

        return n==0


            




        return backtrack(0,0)
        