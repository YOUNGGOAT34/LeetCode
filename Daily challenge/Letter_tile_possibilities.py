from typing import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq=Counter(tiles)

        

        def backtrack()->int:

            res=0
            for char in freq:
                if freq[char]>0:
                    
                    freq[char]-=1
                    res+=1
                    res+=backtrack()
                    freq[char]+=1

            return res

        

        return backtrack()
        