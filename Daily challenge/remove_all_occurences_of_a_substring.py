class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        while part in s:
            for i in range(len(s)-len(part)+1):
                window=s[i:i+len(part)]

                if window==part:
                    s=s.replace(window,"",1)

        return s