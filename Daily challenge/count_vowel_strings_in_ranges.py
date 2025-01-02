class Solution(object):
    def vowelStrings(self, words, queries):
        vowels=set("aeiou")
        prefixes=[0]*(len(words)+1)
        prev=0
        for i,w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prev+=1
            prefixes[i+1]=prev
        
        res=[0]*len(queries)
        for i,query in enumerate(queries):
            l,r=query
            res[i]=prefixes[r+1]-prefixes[l]
        return res

    
        