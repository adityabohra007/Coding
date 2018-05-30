/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    if ( nums1 == null || nums2 == null ) {
        return null;
    }

    var m = nums1.length - 1;
    var n = nums2.length - 1;
    var index = m + n + 1;
    var point;
    var odd;
    if ( (index + 1) % 2 ) {
        point = (index + 2) / 2 - 1;
        odd = true;
    } else {
        point = (index + 1) / 2 - 1;
        odd = false;
    }

    while ( m >= 0 && n >= 0 ) {
        if ( nums1[m] < nums2[n] ) {
            nums1[index--] = nums2[n--];
        } else {
            nums1[index--] = nums1[m--];
        }
    }

    while ( n >= 0 ) {
        nums1[index--] = nums2[n--];
    }

    if ( odd ) {
        return nums1[point];
    } else {
        return (nums1[point] + nums1[point+1]) / 2;
    }

};