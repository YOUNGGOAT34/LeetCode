class Solution:
    def punishmentNumber(self, n: int) -> int:
        res=0
        def partition(i:int,target:int,curr:int,string:str)->bool:
            if i==len(string) and curr==target:
                return True

            for j in range(i,len(string)):
                
                if partition(j+1,target,curr+int(string[i:j+1]),string):
                    return True

            return False
            
        for i in range(1,n+1):
            if partition(0,i,0,str(i*i)):
                res+=i*i

        return res
        