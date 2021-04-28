function palindromos(max, min = 1) {
    if (parseInt(max) && max > 0) {
        parseInt(max)
    } else {
        max = 0
    }
    let arr = []
    for (min; min <= max; min++) {
        if (min == parseInt(min.toString().split('').reverse().join(''))) arr.push(min)
    }
    return arr
}

// Alternativa um pouco mais funcional
function palindromos2(max, arr = [], min = 1) {
    (parseInt(max) && max > 0) || (max = 0)
    return min <= max ? min == parseInt(min.toString().split('').reverse().join('')) ? palindromos2(max, arr.concat(min), min + 1) : palindromos2(max, arr, min + 1) : arr
}

console.log(palindromos(3010, 3000))

