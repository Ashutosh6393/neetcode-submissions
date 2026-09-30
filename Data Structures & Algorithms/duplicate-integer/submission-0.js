class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let x = [];
        for(let i = 0 ; i<nums.length; i++){
            if(x[nums[i]] !== undefined){
                return true;
            }
            x[nums[i]] = nums[i];
        }

        return false;
    }
}
