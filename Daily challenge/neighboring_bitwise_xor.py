class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        #soln 1
        # res=0

        # for n in derived:
        #     res^=n
        
        
        # return res==0
        #sol 2

        first=0
        last=0

        for n in derived:
            if n:
                last=~last


        return first==last