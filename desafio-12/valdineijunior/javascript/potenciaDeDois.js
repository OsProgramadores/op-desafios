const fs = require("fs");

function readFractions(path) {
  fs.readFile(path, "utf-8", function (error, data) {
    if (error) {
      console.log("erro de leitura: " + error.message);
    } else {
      let numbersArray = [];
      if ((/[\n\r]/.test(data))) {
        numbersArray = data.split("\r\n");
      } else {
        numbersArray = data.split("\n");
      }
      numbersArray.pop();
      for (let i = 0; i < numbersArray.length; i++) {
        const element = numbersArray[i];
        let numberIsAPotentialOfTwo = false;
        let expoent = 0n;
        while ((2n ** expoent) <= element) {
          numberIsAPotentialOfTwo = (2n ** expoent) === BigInt(element);
          expoent++;
        }
        if (numberIsAPotentialOfTwo) {
          expoent = expoent - 1n;
          console.log(element, numberIsAPotentialOfTwo, parseInt(expoent));
        } else {
          console.log(element, numberIsAPotentialOfTwo);
        }
      }
    }
  });
}
readFractions("/d12.txt");
