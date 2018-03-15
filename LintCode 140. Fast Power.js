/**
 * @param a: A 32bit integer
 * @param b: A 32bit integer
 * @param n: A 32bit integer
 * @return: An integer
 */
const fastPower = function (a, b, n) {
    if ( n === 1 ) {
        return a % b;
    }
    if ( n === 0 ) {
        return 1 % b;
    }

    var v = fastPower(a, b, Math.floor(n/2));
    v = ( v * v ) % b;
    if ( n % 2 === 1 ) {
        v =  ( v * a ) % b;
    }
    return parseInt(v);
};