/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    // 从后往前处理，不需要开辟新的空间
    if ( m == 0 ) {
        for ( var i = 0; i < n; i++ ) {
            nums1[i] = nums2[i]
        }
    } else {
        var n1 = m-1;
        var n2 = n-1;
        var n = m+n-1;
        while ( n1>=0 && n2>=0 ) {
            if ( nums1[n1] > nums2[n2] ) {
                nums1[n--] = nums1[n1--];
            } else {
                nums1[n--] = nums2[n2--];
            }
        }
        while ( n2 >= 0 ) {
            nums1[n--] = nums2[n2--];
        }
    }
};