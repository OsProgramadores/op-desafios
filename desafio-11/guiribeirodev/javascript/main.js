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

function getPrimeArray(minPrime, maxPrime) {
    const isPrime = new Array(maxPrime + 1).fill(true);

    isPrime[0] = isPrime[1] = false; // 0 and 1 are not prime numbers

    for (let number = minPrime; number * number <= maxPrime; number++) {
        if (!isPrime[number]) {
            continue;
        }

        for (let multiple = number * number; multiple <= maxPrime; multiple += number) {
            isPrime[multiple] = false;
        }
    }

    return isPrime;
}

function findLongestPrimeSequenceInPi(digitsOfPi, isPrimeArray, minPrime, maxPrime) {
    const digitCount = String(digitsOfPi).length;
    const minSliceLength = String(minPrime).length;
    const maxSliceLength = String(maxPrime).length;

    const bestLengthFromIndex = new Array(digitCount + 1).fill(0);

    function getBestLengthForIndex(currentIndex) {
        let bestLength = 0;

        for (let sliceLength = minSliceLength; sliceLength <= maxSliceLength; sliceLength++) {
            const endIndex = currentIndex + sliceLength;

            if (endIndex > digitCount) {
                break;
            }

            const digitNumber = Number(digitsOfPi.slice(currentIndex, endIndex));

            if (isPrimeArray[digitNumber]) {
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

    const MIN_PRIME = 2;
    const MAX_PRIME = 9973;
    const isPrimeArray = getPrimeArray(MIN_PRIME, MAX_PRIME);

    const longestSequence = findLongestPrimeSequenceInPi(
        digitsOfPi,
        isPrimeArray,
        MIN_PRIME,
        MAX_PRIME
    );

    console.log(longestSequence);
}

main();
