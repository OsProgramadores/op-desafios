function encontrarPalindromos(inicial, final) {
    for (let i = inicial; i <= final; i++) {
        let revertido = i.toString().split("").reverse().join("");
        if(parseInt(revertido) == i) {
            console.log(revertido);
        }
    }
}
encontrarPalindromos(101, 121);