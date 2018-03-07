/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    if ( nums1 == null || nums2 == null ) {
        return null;
    }

    nums1.sort(function(a, b) {
        return a - b;
    });

    nums2.sort(function(a, b) {
        return a - b;
    });

    var i = 0;
    var j = 0;
    var index = 0;
    var result = [];

    while ( i < nums1.length && j < nums2.length ) {
        if ( nums1[i] == nums2[j] ) {
            result[index++] = nums1[i];
            i++;
            j++;
        } else if ( nums1[i] < nums2[j] ) {
            i++;
        } else {
            j++;
        }
    }

    return result;
};