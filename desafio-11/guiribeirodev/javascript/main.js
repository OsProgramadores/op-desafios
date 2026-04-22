import { readFileSync } from "fs";

function extractDigitsOfPi() {
    const filePath = process.argv[2];

    if (!filePath) {
        console.error(
            "Insira o caminho do arquivo. Exemplo: node main.js pi-1M.txt"
        );
        process.exit(1);
    }

    return readFileSync(filePath, "utf-8").slice(2);
}

function getPrimeSet(minPrime, maxPrime) {
    const primeSet = new Set();

    const isPrime = new Array(maxPrime + 1).fill(true);
    isPrime[0] = isPrime[1] = false; // 0 and 1 are not prime numbers

    for (let number = 2; number * number <= maxPrime; number++) {
        if (!isPrime[number]) {
            continue;
        }

        for (let multiple = number * number; multiple <= maxPrime; multiple += number) {
            isPrime[multiple] = false;
        }
    }

    for (let number = minPrime; number <= maxPrime; number++) {
        if (isPrime[number]) {
            primeSet.add(number);
        }
    }

    return primeSet;
}

function findLongestPrimeSequenceInPi(digitsOfPi, primeSet) {
    const digitCount = digitsOfPi.length;
    const bestLengthFromIndex = new Array(digitCount + 1).fill(0);

    function getBestLengthForIndex(currentIndex) {
        let bestLength = 0;

        for (let sliceLength = 1; sliceLength <= 4; sliceLength++) {
            const endIndex = currentIndex + sliceLength;

            if (endIndex > digitCount) {
                break;
            }

            const digitNumber = Number(digitsOfPi.slice(currentIndex, endIndex));

            if (primeSet.has(digitNumber)) {
                const candidateLength = sliceLength + bestLengthFromIndex[endIndex];

                if (candidateLength > bestLength) {
                    bestLength = candidateLength;
                }
            }
        }

        return bestLength;
    }

    let longestLength = 0;
    let startIndex = -1;

    for (let digitIndex = digitCount - 1; digitIndex >= 0; digitIndex--) {
        const currentBestLength = getBestLengthForIndex(digitIndex);

        bestLengthFromIndex[digitIndex] = currentBestLength;

        if (currentBestLength >= longestLength) {
            longestLength = currentBestLength;
            startIndex = digitIndex;
        }
    }

    const longestSequence = digitsOfPi.substring(
        startIndex,
        startIndex + longestLength
    );

    return longestSequence;
}

function main() {
    const digitsOfPi = extractDigitsOfPi();

    const minimumPrime = 2;
    const maximumPrime = 9973;
    const primeSet = getPrimeSet(minimumPrime, maximumPrime);

    const longestSequence = findLongestPrimeSequenceInPi(digitsOfPi, primeSet);

    console.log(longestSequence);
}

main();
