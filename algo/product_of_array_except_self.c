#include<stdio.h>

//brute force solution;
// int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
      
//    int *ret=malloc(sizeof(int)*numsSize);
//    *returnSize=0;

//    for(int i=0;i<numsSize;i++){
//        int prod=1;
//        for(int j=0;j<numsSize;j++){
//            if(i==j){
//                continue;
//            }
         
//           prod*=nums[j];
          

//        }

//        ret[*returnSize]=prod;
//        (*returnSize)++;
//    }

//    return ret;
// }


//total product then divide by the sel

// int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
      
//    int *ret=malloc(sizeof(int)*numsSize);
//  //   int *prefix=malloc(sizeof(int)*numsSize);
//  //   int *suffix=malloc(sizeof(int)*numsSize);
//    *returnSize=0;
//   int prod=1;

//     for(int i=0;i<numsSize;i++){
//         prod*=nums[i];
//     }

//     for(int i=0;i<numsSize;i++){
//          ret[*returnSize]=prod/nums[i];

//          *returnSize=i;
//     }

//  //   memset() 

//  //   free(prefix);
//  //   free(suffix);
//    return ret;
// }


/*
  prefix,suffix 
*/
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
      
   int *ret=malloc(sizeof(int)*numsSize);
   int *prefix=malloc(sizeof(int)*numsSize);
   int *suffix=malloc(sizeof(int)*numsSize);
   *returnSize=numsSize;
    



   
   prefix[0]=1;

   for(int i=1;i<numsSize;i++){
       prefix[i]=nums[i-1]*prefix[i-1];
   }

   suffix[numsSize-1]=1;
   
   for(int i=numsSize-2;i>=0;i--){
       suffix[i]=nums[i+1]*suffix[i+1];
   }

   for(int i=0;i<numsSize;i++){
       ret[i]=suffix[i]*prefix[i];
   }


   free(prefix);
   free(suffix);
   return ret;
}