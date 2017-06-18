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

    var results = [];
    if( nums == null || nums.length == 0 ) {
        return results;
    }

    var subset = [];

    nums.sort(compare);

    function compare(v1, v2) {
        return v1 - v2;
    }

    permuteHelper( nums, subset, results );

    return results;

    function permuteHelper( nums, subset, results ) {
        if( subset.length == nums.length ){
            results.push(subset.slice());
        } else {
            for( var i = 0; i < nums.length; i++ ){
                if( subset.indexOf(nums[i]) > -1 ){
                    continue;
                }
                subset.push(nums[i]);
                permuteHelper(nums, subset, results);
                subset.pop();
            }
        }
    }
};