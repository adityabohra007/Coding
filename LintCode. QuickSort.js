var quickSort_1 = function (A) {
    quickSort(A, 0, A.length-1);

    console.log(A);
};

var quickSort = function (A, start, end) {
    if ( start >= end ) {
        return;
    }

    var left = start;
    var right = end;
    var pivot = A[Math.floor( (left+right)/2 )];

    while ( left <= right ) {
        while ( left <= right && A[left] < pivot ) {
            left++;
        }

        while ( left <= right && A[right] > pivot ) {
            right--;
        }

        if ( left <= right ) {
            var tmp = A[left];
            A[left] = A[right];
            A[right] = tmp;

            left++;
            right--;
        }
    }

    quickSort(A, start, right);
    quickSort(A, left, end);

};