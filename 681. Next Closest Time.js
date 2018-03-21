/**
 * @param {string} time
 * @return {string}
 */
/**
 * 先将 time 中的每个数字从大到小存入数组 timeArr 中
 * 然后从后依次比较 time 中的每个数字，如果这个数字不是最大的，从数组 timeArr 中取出下一个比它大的，直接返回结果（其他位置不变）
 * 如果这个数字是最大的，就取最小的数字，再往前比较
 */
var nextClosestTime = function(time) {
    var timeArr = [];
    var result = time;
    for (var i = 0; i < time.length; i++){
        if ( !isNaN(time[i]) ){
            if (timeArr.indexOf(parseInt(time[i])) < 0) {
                timeArr.push(parseInt(time[i]));
            }
        }
    }

    timeArr.sort(function (a, b){
        return a - b;
    });

    var n = timeArr.length - 1;

    for (var j = result.length - 1; j >= 0; j--) {
        if (result[j] == ':') {
            continue;
        }
        var number = parseInt(result[j]);
        var position = timeArr.indexOf(number);
        if ( position == n ) {
            result =  result.substr(0, j) + timeArr[0] + result.substring(j+1);
        } else {
            var v = timeArr[position+1];
            if (j == 4) {
                result =  result.substr(0, j) + v + result.substring(j+1);
                return result;
            } else if (j == 3 && v <= 5) {
                result =  result.substr(0, j) + v + result.substring(j+1);
                return result;
            } else if (j == 1 && (result[j-1] != 2 || (result[j-1] == 2 && v <= 4))) {
                result =  result.substr(0, j) + v + result.substring(j+1);
                return result;
            } else if (j == 0 && v <= 2) {
                result =  result.substr(0, j) + v + result.substring(j+1);
                return result;
            }
            result =  result.substr(0, j) + timeArr[0] + result.substring(j+1);
        }
    }

    return result;

};