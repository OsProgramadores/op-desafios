function isPrimo(num) {

    for (let i = 2; i <= num; i++) {
        if (num % i === 0){
            return false;
        }
        return num > 1;
    }
}

let arr = [2];
let numEntrada = 10000;

for (let i = 3; i < numEntrada; i++){
    if (isPrimo(i) === true){
        arr.push(i);
    }
}
console.log(arr)
