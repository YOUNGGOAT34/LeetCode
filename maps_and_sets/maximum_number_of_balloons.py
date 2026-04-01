class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        Map=defaultdict(int)

        for c in text:
            Map[c]+=1

        return min(
            Map["b"],
            Map["a"],
            Map["l"]//2,
            Map["o"]//2,
            Map['n']
        )

        

        