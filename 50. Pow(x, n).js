/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    if ( n < 0 ) {
        return 1/power(x, -n);
    } else {
        return power(x, n);
    }
};

var power = function (x, n) {
    if ( n == 1 ) {
        return x;
    }
    if ( n == 0 ) {
        return 1;
    }

    var value = power(x, Math.floor(n/2));

    if ( n%2 == 0 ) {
        return value * value;
    } else {
        return value * value * x;
    }
}