class Solution {
    public int findClosestNumber(int[] nums) {
        int closest=nums[0];
        for(int num:nums){
            if(Math.abs(num)<Math.abs(closest)) closest=num;  
        }

        if(closest<0&&contains(nums,Math.abs(closest))){
            return Math.abs(closest);
        }else{
            return closest;
        }
    }

    private boolean contains(int[] array,int number){
        for(int num:array){
            if(num==number) return true;
        }
        return false;
    }
}