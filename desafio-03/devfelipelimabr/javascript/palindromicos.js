//353
const isPal = (num) => {
    const strg = String(num);
    let firstIndex = 0;
    let lastIndex = strg.length - 1;
    let result;

    if (strg.length === 1) {
        result = true
    } else {
        if (strg.length % 2 === 0) {
            for (let i = strg.length / 2; i > 0; i--) {
                if (strg[firstIndex] == strg[lastIndex]) {
                    result = true;
                    firstIndex++
                    lastIndex--
                } else {
                    result = false;
                    i = 0;
                }
            }
        } else {
            for (let i = strg.length / 2; i > 1; i--) {
                if (strg[firstIndex] == strg[lastIndex]) {
                    result = true;
                    firstIndex++
                    lastIndex--
                } else {
                    result = false;
                    i = 0;
                }
            }
        }
    }
    return result;
}

let arr = [];
const firstNum = 11;
const lastNum = 10000;

if (Number.isInteger(firstNum) === true && Number.isInteger(lastNum) === true && firstNum < lastNum && firstNum > 0 && lastNum < 4294967295) {
    for (let i = firstNum; i <= lastNum; i++) {
        if (isPal(i) === true) {
            arr.push(i);
        }
    }
    console.log(arr);
} else {
    console.log(`Digite valores válidos`)
}