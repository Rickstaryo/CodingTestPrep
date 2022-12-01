function solution(array, height) {
    var answer = 0;
    for(var i in array){
        var h = array[i];
        if(height < h){
            answer++;
        }
    }
    return answer;
}