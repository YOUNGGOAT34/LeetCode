#include<stdio.h>

int removeDuplicates(int* nums, int numsSize) {
    
   if(numsSize==0) return 0;

    int i=1,j=1;
     
     while(i<numsSize){
         
         while(i<numsSize && nums[i]==nums[i-1]){
            i++;
         }

         if(i<numsSize){

         nums[j]=nums[i];
         j++;
         i++;
         }
     }

    return j;
}