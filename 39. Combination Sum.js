/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    var result = [];
    if ( candidates == null || candidates.length == 0 ) {
        return result;
    }

    var nums = removeDuplicated( candidates );
    dfs ( nums, target, result, 0, [] );

    return result;

    function removeDuplicated ( arr )
    {
        arr.sort(function(a,b){return a>b?1:-1});

        var index = 0;
        for ( var i = 0; i < arr.length; i++ ) {
            if ( arr[i] != arr[index] ) {
                index++;
                arr[index] = arr[i];
            }
        }

        var nums = [];
        for ( var j = 0; j < index + 1; j++ ) {
            nums[j] = arr[j];
        }

        return nums;
    }

    function dfs ( nums, target, result, startIndex, temp )
    {
        if ( target == 0 ) {
            result.push( temp.slice() );
            return;
        }

        for ( var i = startIndex; i < nums.length; i++ ) {
            if ( target < nums[i] ) {
                break;
            }

            temp.push( nums[i] );
            dfs ( nums, target - nums[i], result, i, temp );
            temp.pop();
        }
    }
};