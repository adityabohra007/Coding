/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    var result = [];

    if( nums == null || nums.length == 0 ){
        return result;
    }

    // sort
    nums.sort();

    var subset = [];
    subsetHelper(nums, 0, subset, result);

    function subsetHelper(nums, startIndex, subset, result) {

        result.push(subset.slice());

        for( var i = startIndex; i < nums.length; i++ ){
            if( i != 0 && nums[i] == nums[i-1] && i > startIndex ){
                continue;
            }
            subset.push(nums[i]);
            subsetHelper( nums, i + 1, subset, result );
            subset.pop();
        }
    }

    return result;
};