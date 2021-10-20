const numerosPrimos = (x, y) => {
    for (let n = x; n <= y; n++) {
        let c = 0;
        for (let i = n; i >= 1; i--) {
            if (n % i == 0) {
                c++;
            }
        }
        c == 2 && console.log(n);
    }
}

numerosPrimos(1, 100);