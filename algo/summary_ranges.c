
#include<stdio.h>

char** summaryRanges(int* nums, int numsSize, int* returnSize) {
   char **ranges=(char **)malloc(sizeof(char *)*numsSize);
    
    *returnSize=0;
      
      int i=0;
      int start=nums[0],end=start;
      
      while(i<numsSize){
        start=nums[i];
        while(i<numsSize-1 && nums[i+1]==nums[i]+1){
             i++;
         }

         end=nums[i];
         
          ranges[*returnSize]=(char *)malloc(25);

         if(start==end){
            sprintf(ranges[*returnSize],"%d",start);
         }else{
             sprintf(ranges[*returnSize],"%d->%d",start,end);
         }
        
         
          (*returnSize)++;
         i++;
      }


  
   return ranges;
}