/**
 * @param {number[]} nums
 * @return {number}
 */
var findClosestNumber = function(nums) {
    let closest=nums[0]
    for(const num of nums){
        if(Math.abs(num)<Math.abs(closest)){
            closest=num
        }
    }
    if(closest<0&&nums.includes(Math.abs(closest))){
        return Math.abs(closest)
    }
    return closest
};