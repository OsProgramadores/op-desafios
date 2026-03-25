//let num = 18446744073709552000
let num = 50
for (let i = 0; i<=num; i++){
    let isPalindromo = true;
    let str = i.toString().split("");
    let size = (str.length-1);
    str.forEach( (c, index) => {
        (str[size-index] != str[size]) ? isPalindromo=false : null
    })
    isPalindromo ? console.log(str.join("")) : null;
}