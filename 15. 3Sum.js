/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {

    var result = [];
    if ( nums == null || nums.length < 3 ) {
        return result;
    }

    nums.sort(function(a, b){
        return a - b;
    });

    for ( var i = 0; i < nums.length - 2; i++ ) {
        if ( i > 0 && nums[i] == nums[i-1] ) {
            continue;
        }

        var left = i+1;
        var right = nums.length-1;
        var target = -nums[i];

        findTwoSum( nums, target, left, right, result );

    }
    return result;
};

var findTwoSum = function( nums, target, left, right, result ) {
    console.log('left:: '+left+' right:: '+right);
    while ( left < right ) {
        if ( nums[left] + nums[right] == target ) {
            var ret = [];
            ret.push(-target);
            ret.push(nums[left]);
            ret.push(nums[right]);
            result.push(ret);

            left++;
            right--;

            while ( left < right && nums[left] == nums[left-1] ) {
                left++;
            }

            while ( left < right && nums[right] == nums[right+1] ) {
                right--;
            }
        } else if ( nums[left] + nums[right] < target ) {
            left++;
        } else {
            right--;
        }
    }
}