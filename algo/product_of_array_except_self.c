#include<stdio.h>

//brute force solution;
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
      
   int *ret=malloc(sizeof(int)*numsSize);
   *returnSize=0;

   for(int i=0;i<numsSize;i++){
       int prod=1;
       for(int j=0;j<numsSize;j++){
           if(i==j){
               continue;
           }
         
          prod*=nums[j];
          

       }

       ret[*returnSize]=prod;
       (*returnSize)++;
   }

   return ret;
}