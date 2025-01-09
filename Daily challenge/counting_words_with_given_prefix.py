class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        L=len(pref)
        res=0
        for word in words:

            if word[:L]==pref:#startswith can also be used
                res+=1

        return res
        