/**
 * @param {number[]} nums
 * @return {number[][]}
 */
/**
 * 跟 Permutations的解法一样，
 * 就是要考虑“去重”。先对数组进行排序，这样在DFS的时候，可以先判断前面的一个数是否和自己相等，
 * 相等的时候则前面的数必须使用了，自己才能使用，这样就不会产生重复的排列了。
 */
var permuteUnique = function(nums) {
    var result = [];
    if ( nums == null || nums.length == 0 ) {
        return result;
    }

    nums.sort(compare);

    function compare ( v1, v2 ) {
        return v1 - v2;
    }

    dfs ( nums, result, [], [] );

    return result;

    function dfs ( nums, result, tmp, ref )
    {
        if ( tmp.length == nums.length ) {
            result.push(tmp.slice());
            return;
        }

        for ( var i = 0; i < nums.length; i++ ) {
            if ( ref.indexOf(i) > -1 || ( i > 0 && nums[i] == nums[i - 1] && ref.indexOf(i-1) < 0 ) ) {
                continue;
            }

            ref.push(i);
            tmp.push(nums[i]);
            dfs( nums, result, tmp, ref );
            ref.pop();
            tmp.pop();
        }
    }
};