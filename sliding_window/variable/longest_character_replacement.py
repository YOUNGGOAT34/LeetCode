class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency_array=[0]*26

        left=0
        max_freq=0
        res=0
     
        for right in range(len(s)):
            frequency_array[ord(s[right])-ord('A')]+=1
            max_freq=max(max_freq,frequency_array[ord(s[right])-ord('A')])
            while ((right-left)+1)-max_freq>k:
                frequency_array[ord(s[left])-ord('A')]-=1
                left+=1

            res=max(res,right-left+1)


        return res
