/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {

    var degree = new Array(numCourses);
    var edges = new Array(numCourses);

    for ( var i = 0; i < numCourses; i ++ ) {
        degree[i] = 0;
    }

    for ( var i = 0; i < numCourses; i ++ ) {
        edges[i] = [];
    }

    for ( var j = 0; j < prerequisites.length; j++ ) {
        degree[prerequisites[j][0]] ++;
        edges[prerequisites[j][1]].push(prerequisites[j][0]);
    }

    // 挑出没有前置课程的课
    var queue = [];
    for ( var k = 0; k < degree.length; k ++ ) {
        if ( degree[k] == 0 ) {
            queue.push( k );
        }
    }

    var count = 0;

    while ( queue.length > 0 ) {
        var course = queue.shift();
        count ++;
        // n ->  这个课程有多少个后续课程
        var n = edges[course].length;
        for ( var l = 0; l < n; l ++ ) {
            var pointer = edges[course][l];
            degree[pointer] --;
            if ( degree[pointer] == 0 ){
                queue.push(pointer);
            }
        }
    }

    return count == numCourses;
};