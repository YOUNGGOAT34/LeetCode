class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_words2=defaultdict(int)

        for w in words2:
            count_w=Counter(w)

            for word,count in count_w.items():
                count_words2[word]=max(count,count_words2[word])

        res=[]

        for w in words1:
            count_w1=Counter(w)
            flag=True

            for char,count in count_words2.items():
                if count_w1[char]<count:
                    flag=False
                    break

            if flag:
                res.append(w)
                
        return res





        