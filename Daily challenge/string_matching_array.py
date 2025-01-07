class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]

        for i,word in enumerate(words):
            for j in range(len(words)):
                if i==j:
                    continue
                else :
                    if word in words[j]:
                        res.append(word)
                        break

        return res
        