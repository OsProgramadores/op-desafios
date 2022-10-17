for (let i = 1; i <= 10000; i++) {
    let numberOfMultiples = 0
    for (let j = 1; j <= i; j++) {
        if (i%j == 0) {
            numberOfMultiples++
        }
    }
    if (numberOfMultiples == 2) {
        console.log(i)
    }
}