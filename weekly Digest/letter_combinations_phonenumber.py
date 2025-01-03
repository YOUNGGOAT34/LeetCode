class Solution:
    def letterCombinations(self, digits)->List[str]:
        res=[]
        phone_keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if  digits=="":
            return res
        def backtrack(i:int,current_solution:str)->None:
            
              if(len(current_solution)==len(digits)):
                 res.append(current_solution)
                 return
              for character in phone_keypad[digits[i]]:
                  
                  backtrack(i+1,current_solution+character) 

        backtrack(0,"")

        return res
        