/**
 * @param colors: A list of integer
 * @param k: An integer
 * @return:
 */
const sortColors2 = function (colors, k) {
    if ( colors === null || colors.length === 0 ) {
        return colors;
    }

    rainbowSort(colors, 0, colors.length-1, 1, k);
}

const rainbowSort = function (colors, left, right, colorFrom, colorTo) {
    if ( colorFrom == colorTo ) {
        return;
    }

    if ( left >= right ) {
        return;
    }

    var mid = Math.floor((colorFrom+colorTo)/2);
    var l = left;
    var r = right;
    while ( l <= r ) {
        while ( l <= r && colors[l] <= mid ) {
            l++;
        }
        while ( l <= r && colors[r] > mid ) {
            r--;
        }
        if ( l <= r ) {
            var tmp = colors[l];
            colors[l] = colors[r];
            colors[r] = tmp;

            l++;
            r--
        }
    }
    rainbowSort(colors, left, r, colorFrom, mid);
    rainbowSort(colors, l, right, mid+1, colorTo);
}

