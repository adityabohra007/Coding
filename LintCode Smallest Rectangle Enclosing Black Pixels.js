var minArea = function (images, x, y) {

    var n = images.length;
    var m = images[0].length;
    if ( images == null || n == 0 ) {
        return 0;
    }

    if ( images[0] == null || m == 0 ) {
        return 0;
    }

    // 最左边到哪里
    var start = 0;
    var end = y;
    var mid;
    while ( start + 1 < end ) {
        mid = start + Math.round( (end - start) / 2 );
        if ( isBlackColumn( images, mid) ){
            end = mid;
        } else {
            start = mid;
        }
    }

    var left = y;
    if ( isBlackColumn( images, end ) ) {
        left = end;
    } else if ( isBlackColumn( images, start ) ) {
        left = start;
    }

    // 最右边到哪里
    start = y;
    end = m - y;
    while ( start + 1 < end ) {
        mid = start + Math.round( (end - start) / 2 );
        if ( isBlackColumn( images, mid ) ){
            start = mid;
        } else {
            end = mid;
        }
    }

    var right = y;
    if ( isBlackColumn( images, start ) ) {
        right = start;
    } else if ( isBlackColumn( images, end ) ) {
        right = end;
    }

    // 最上能到哪里
    start = 0;
    end = x;
    while ( start + 1 < end ) {
        mid = start + Math.round( (end - start) / 2 );
        if ( isBlackRow( images, mid ) ){
            end = mid;
        } else {
            start = mid;
        }
    }

    var top = x;
    if ( isBlackColumn( images, end ) ) {
        top = end;
    } else if ( isBlackColumn( images, start ) ) {
        top = start;
    }

    // 最下能到哪里
    start = x;
    end = n - x;
    while ( start + 1 < end ) {
        mid = start + Math.round( (end - start) / 2 );
        if ( isBlackRow( images, mid) ){
            start = mid;
        } else {
            end = mid;
        }
    }

    var bottom = x;
    if ( isBlackColumn( images, start ) ) {
        bottom = start;
    } else if ( isBlackColumn( images, end ) ) {
        bottom = end;
    }


    //console.log('right = '+right+' left = '+left+' top = '+top+' bottom = '+bottom);
    return ( right - left + 1 ) * ( bottom - top + 1 );

    function isBlackColumn( images, c ) {
        for ( var i = 0; i < n; i++ ) {
            if( images[c][i] == 1 ){
                return true;
            }
        }
        return false;
    }

    function isBlackRow( images, r ) {
        for ( var i = 0; i < m; i++ ) {
            if( images[i][r] == 1 ){
                return true;
            }
        }
        return false;
    }

};