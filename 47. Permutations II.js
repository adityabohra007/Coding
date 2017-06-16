/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    var results = [];
    if( nums == null || nums.length == 0 ) {
        return results;
    }

    var subset = [];
    var ref= [];

    nums.sort();

    permuteUniqueHelper( nums, subset, ref, results );

    return results;

    function permuteUniqueHelper( nums, subset, ref, results ) {
        if( subset.length == nums.length ){
            results.push(subset.slice());
        } else {
            for( var i = 0; i < nums.length; i++ ){
                if( ref.indexOf(i) > -1 || (i > 0 && nums[i] == nums[i-1] && ref.indexOf(i-1) < 0) ){
                    continue;
                }
                ref.push(i);
                subset.push(nums[i]);
                permuteUniqueHelper(nums, subset, ref, results);
                ref.pop();
                subset.pop();
            }
        }
    }
};