class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0
        number_of_balls_to_recolor=0
        res=k

        for right in range(len(blocks)):
            if blocks[right]=="W":
                number_of_balls_to_recolor+=1

            if (right-left)+1==k:
                res=min(res,number_of_balls_to_recolor)
                if blocks[left]=="W":
                    number_of_balls_to_recolor-=1

                left+=1


        return res
        


        