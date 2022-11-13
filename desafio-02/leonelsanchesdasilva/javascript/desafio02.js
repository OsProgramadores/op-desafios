for (let i = 1; i <= 10000; i++) {
    let primo = true;
    for (let j = 2; j <= Math.floor(Math.sqrt(i)); j++) {
        if (i % j === 0) {
            primo = false;
            break;
        }
    }

    if (primo) {
        console.log(i);
    }
}