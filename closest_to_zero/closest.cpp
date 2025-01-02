#include<iostream>
#include<algorithm>
#include<vector>

class Solution {
public:
    int findClosestNumber(std::vector<int>& nums) {
        int closest=nums[0];
        
        for(auto num:nums){
             if(abs(num)<abs(closest)) closest=num;
        }
        
        if(closest<0&&std::find(nums.begin(),nums.end(),abs(closest))!=nums.end()){
            return abs(closest);
        }else{
            return closest;
        }
        
    }
};