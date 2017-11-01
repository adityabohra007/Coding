/*
 Given a collection of distinct numbers, return all possible permutations.

 For example,
 [1,2,3] have the following permutations:

 [
 [1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]
 ]

 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    var result = [];

    if ( nums == null || nums.length == 0 ) {
        return result;
    }

    dfs( nums, result, [] );

    return result;

    function dfs ( nums, result, tmp )
    {
        if ( tmp.length == nums.length ) {
            result.push(tmp.slice());
        }

        for ( var i = 0; i < nums.length; i++ ) {
            if ( tmp.indexOf(nums[i]) > -1 ) {
                continue;
            }
            tmp.push(nums[i]);
            dfs( nums, result, tmp );
            tmp.pop();
        }
    }
};