/**
 * @param {number[]} org
 * @param {number[][]} seqs
 * @return {boolean}
 */
var sequenceReconstruction = function(org, seqs) {

    var map = new Map();
    var indegree = new Map();

    org.forEach(function (num) {
        indegree.set(num, 0);
        map.set(num, []);
    });

    var n = org.length;
    var count = 0;

    for ( var i = 0; i < seqs.length; i++ ) {
        count += seqs[i].length;
        // seq 只有一个数的情况
        if ( seqs[i].length == 1 ) {
            if ( seqs[i][0] < 0 || seqs[i][0] > n ) {
                return false;
            }
        } else if ( seqs[i].length > 1 ) {
            // seq 有多个数
            if ( seqs[i][0] < 0 || seqs[i][0] > n ) {
                return false;
            }
            for ( var j = 1; j < seqs[i].length; j++ ) {
                if ( seqs[i][j] < 0 || seqs[i][j] > n ) {
                    return false;
                }
                var followingNums = map.get(seqs[i][j-1]);
                if ( followingNums.indexOf(seqs[i][j]) < 0 ) {
                    followingNums.push(seqs[i][j]);
                    map.set(seqs[i][j-1], followingNums);
                    indegree.set(seqs[i][j], indegree.get(seqs[i][j])+1)
                }
            }
        }
    }

    if ( count < n ) {
        return false;
    }

    var q = [];
    for ( var k of indegree.keys() ) {
        if ( indegree.get(k) == 0 ) {
            q.push(k)
        }
    }

    var cnt = 0;
    while ( q.length == 1 ) {
        var number = q.shift();
        for ( var next of map.get(number) ) {
            indegree.set(next, indegree.get(next)-1);
            if ( indegree.get(next) == 0 ) {
                q.push(next);
            }
        }
        if ( number != org[cnt] ) {
            return false;
        }
        cnt++;
    }

    return cnt == org.length;

};