let start = 1;
let ending = 622;

for (let index = start; index < ending; index++){
    var array = index.toString().split("");
    if(test(array)){
        console.log(index);
    }
}

function test(array){
    var i = 0;
    var j = array.length - 1;

    while (i < j) {
        if (array[i] != array[j]) {
            return false;
        } else {
            i++;
            j--;
        }
    }
    return true;
}