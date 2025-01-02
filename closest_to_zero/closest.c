#include<stdio.h>
#include<stdbool.h>


bool contains(int *array,int size,int target){
   for(int i=0;i<size;i++){
     if(array[i]==target) return true;
   }
   return false;
}

int findClosestNumber(int* nums, int numsSize) {
    int closest=nums[0];
    for(int i=0;i<numsSize;i++){
        if(abs(nums[i])<abs(closest)){
            closest=nums[i];
        }
    }
    if(closest<0&&contains(nums,numsSize,abs(closest))){
        return abs(closest);
    }
    return closest;
}

