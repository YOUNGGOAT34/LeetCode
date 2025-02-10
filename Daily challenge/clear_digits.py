class Solution:
    def clearDigits(self, s: str) -> str:
        # a stack to pop a character from whenever I encounter a digit,and append whenever i haven't met any digit
        res=[]

        for i in range(len(s)):
            if s[i].isdigit():
                res.pop()
            else:
                res.append(s[i])


        return "".join(res)
        