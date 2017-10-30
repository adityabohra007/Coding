/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    var result = [];
    if ( candidates == null || candidates.length == 0 ) {
        return result;
    }

    // sort
    var nums = removeDuplicates(candidates);
    dfs ( nums, target, 0, [], result );

    return result;

    function removeDuplicates ( candidates )
    {
        candidates.sort(function(a, b) { return a > b? 1: -1; });

        return candidates;
    }

    function dfs ( nums, target, startIndex, temp, result )
    {
        if ( target == 0 ) {
            result.push(temp.slice());
            return;
        }

        for ( var i = startIndex; i < nums.length; i++ ) {
            if ( i != startIndex && nums[i] == nums[i-1] ) {
                continue;
            }
            if ( target < nums[i] ) {
                break;
            }

            temp.push( nums[i] );
            dfs( nums, target - nums[i], i + 1, temp, result );
            temp.pop();
        }
    }
};