



from typing import List


def prefixSum(nums:List[int])->List[int]:
   ans=[0]*len(nums)

   prefix=0

   for i in range(len(nums)):
      prefix+=nums[i]
      ans[i]=prefix
     

   return ans



def query(start:int,end:int,prefix:List[int]):
 
   return prefix[end]-prefix[start-1]


def main():
   nums=[2,4,6,8]
   prefix=0
   ans=[0]*len(nums)

   for i in range(len(nums)):
      prefix+=nums[i]
      ans[i]=prefix
   print(query(1,3,ans))

if __name__ == "__main__":
    main()
   
    
    
   