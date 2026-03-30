class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        counter=defaultdict(int)

        for c in magazine:
            counter[c]+=1

        for c in ransomNote:
            if not counter[c]:
                return False
            else:
                counter[c]-=1

        return True