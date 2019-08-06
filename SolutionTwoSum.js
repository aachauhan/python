/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(var i = 0; i < nums.length; i++){
        // let indexOne = nums[i];
        // let indexTwo = nums[i+1];
        // let sum = indexOne + indexTwo;
        // if(sum == target){
        //     return [i, i+1];
        // }
        for(var k = i+1; k < nums.length; k++){
            let sum = nums[i] + nums[k];
            if(sum == target){
                return [i, k];
            }
        }
    }
};