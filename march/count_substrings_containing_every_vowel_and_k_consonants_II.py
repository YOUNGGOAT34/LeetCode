from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # exactly k= more than k-k??

        def substringsWithAtleast(k):
            left=0
            sett={"a","e","i","o","u"}
            vowelsCount=defaultdict(int)
            consonants=0
            res=0

            for right in range(len(word)):
                if word[right] in sett:
                    vowelsCount[word[right]]+=1
                else:
                    consonants+=1
                
                while len(vowelsCount)==5 and consonants>=k:
                    res+=(len(word)-right)
                    if word[left] in sett:
                        vowelsCount[word[left]]-=1
                    else:
                        consonants-=1

                    if vowelsCount[word[left]]==0:
                        vowelsCount.pop(word[left])
                    left+=1

            return res


        return substringsWithAtleast(k)-substringsWithAtleast(k+1)
        