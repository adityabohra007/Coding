/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if( needle.length == 0  ){
        return 0;
    }

    if( needle.length > haystack.length ){
        return -1;
    }

    // magic number
    var base = 1000000;
    var l = needle.length;

    // 31 ^ m
    var power = 1;
    for( var i = 0; i < l; i++ ){
        power = (power * 31) % base;
    }

    // 设置 needle 的 hash function的值
    var needleCode = 0;
    for ( i = 0; i < l; i++ ){
        needleCode = (needleCode * 31 + needle.charAt(i).charCodeAt()) % base;
    }

    var haystackCode = 0;
    for (i = 0; i < haystack.length; i++){
        // abc + d
        haystackCode = (haystackCode * 31 + haystack.charAt(i).charCodeAt()) % base;

        if( i < l -1 ){
            continue;
        }

        //    i
        // abcd -a
        if( i >= l ){
            haystackCode = haystackCode - (haystack.charAt(i-l).charCodeAt() * power) % base;
            if( haystackCode < 0 ){
                haystackCode += base;
            }
        }

        if( haystackCode == needleCode ){
            // double check
            if( haystack.substr(i-l+1, l) == needle ){
                return i - l + 1;
            }
        }
    }

    return -1;
};