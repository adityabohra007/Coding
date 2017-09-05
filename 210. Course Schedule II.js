/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    var coursePriority = [];
    var courseSubsequent = [];

    for ( var i = 0; i < numCourses; i ++ ) {
        coursePriority[i] = 0;
        courseSubsequent[i] = [];
    }

    for ( var j = 0; j < prerequisites.length; j++ ) {
        coursePriority[prerequisites[j][0]] ++;
        courseSubsequent[prerequisites[j][1]].push(prerequisites[j][0]);
    }

    var queue = [];
    for ( var k = 0; k < coursePriority.length; k++ ) {
        if ( coursePriority[k] == 0 ) {
            queue.push(k);
        }
    }

    var result = [];
    while ( queue.length > 0 ) {
        var course = queue.shift();
        result.push( course );
        var n = courseSubsequent[course].length;
        if ( n > 0 ) {
            for ( var l = 0; l < n; l ++ ) {
                var pointer = courseSubsequent[course][l];
                coursePriority[pointer]--;
                if ( coursePriority[pointer] == 0 ) {
                    queue.push(pointer);
                }
            }
        }
    }

    if ( result.length == numCourses ) {
        return result
    } else {
        return [] ;
    }
};