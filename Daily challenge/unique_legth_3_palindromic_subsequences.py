class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=set()
        left=set()
        right=Counter(s)

        for mid in s:#m to act as the middle
            right[mid]-=1
            for char in left:
                if right[char]>0:
                    res.add((mid,char))

            left.add(mid)

        return len(res)




        

        