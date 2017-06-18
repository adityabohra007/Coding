var searchBigSortedArray = function (reader, target) {
    var index = 1;
    while ( reader.get(index) < target ) {
        index *= 2;
    }

    var start = 0;
    var end = index - 1;
    var mid;

    while ( start + 1 < end ) {
        mid = start + Math.round( (end - start) / 2 );
        if ( reader.get(mid) >= target ) {
            end = mid;
        } else {
            start = mid;
        }
    }

    if ( reader.get(start) == target ) {
        return start;
    } else if ( reader.get(end) == target ) {
        return end;
    } else {
        return -1;
    }
};