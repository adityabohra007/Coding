/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    var result = [];
    if ( numbers == null || numbers.length == 0 ) {
        return result;
    }

    var map = new Map();
    for ( var i = 0; i < numbers.length; i++ ) {
        map.set(numbers[i], i);
    }

    for ( var j = 0; j < numbers.length; j++ ) {
        var searched = target - numbers[j];
        if ( map.has(searched) && map.get(searched) != j ) {
            var index = map.get(searched);
            if ( index < j ) {
                return [index+1, j+1];
            } else {
                return [j+1, index+1];
            }
        }
    }
};