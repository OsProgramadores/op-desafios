function palindromos(max) {
    if (parseInt(max) && max > 0) {
        parseInt(max)
    } else {
        max = 0
    }
    let arr = []
    for (let num = 1; num <= max; num++) {
        if (num == parseInt(num.toString().split('').reverse().join(''))) arr.push(num)
    }
    return arr
}

// Alternativa um pouco mais funcional
function palindromos2(max, arr = [], num = 1) {
    (parseInt(max) && max > 0) || (max = 0)
    return num <= max ? num == parseInt(num.toString().split('').reverse().join('')) ? palindromos2(max, arr.concat(num), num + 1) : palindromos2(max, arr, num + 1) : arr
}
