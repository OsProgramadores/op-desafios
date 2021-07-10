function palindromos(max, min = 1) {
    let arr = []
    for (min; min <= max; min++) {
        if (min == [...(""+min)].reverse().join('')) arr.concat([min])
    }
    return arr
}
console.log(palindromos(3010, 3000))
