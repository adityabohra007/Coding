/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr1 = function(haystack, needle) {
    if( haystack == null || needle == null || needle.length > haystack.length ) {
        return -1;
    }

    if( needle.length == 0 ){
        return 0;
    }

    var l1 = haystack.length;
    var l2 = needle.length;

    //    de
    // abcdefg
    for ( var i = 0; i < l1 - l2; i++ ){
        for ( var j = 0; j < l2; j++ ){
            if ( haystack.charAt(i+j) !== needle.charAt(j) ){
                break;
            }
            return i;
        }
    }
    return -1;
};