#include<stdio.h>
#include<stdbool.h>

bool contains(int *nums,int target,int size){
    for(int i=0;i<size;i++){
        if(nums[i]==target) return true;
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

    if(closest<0 && contains(nums,abs(closest),numsSize)){
       return abs(closest);
    }

    return closest;
}

