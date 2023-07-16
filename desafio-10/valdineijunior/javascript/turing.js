const fs = require("fs");

function processFile(filename) {
    const rulesAndInputFile = fs.readFileSync(filename, "utf8");
    let rulesAndInput = "";
    if ((/(\r)/.test(rulesAndInputFile))) {
        rulesAndInput = rulesAndInputFile.split("\r\n");
    } else {
        rulesAndInput = rulesAndInputFile.split("\n");
    }
    rulesAndInput.pop();

    for (const line of rulesAndInput) {
        const [rulesFilePath, input] = line.split(",");
        const rules = filteredRules(rulesFilePath);
        turningMachine(rulesFilePath, rules, input);
    }
}

function filteredRules(rulesFileName) {
    const fileRules = fs.readFileSync(rulesFileName, "utf-8").split("\n");
    const filteredLines = fileRules
        .filter(line => line.trim() !== "" && !line.startsWith(";"))
        .map(line => {
            const lineWithoutComments = line.split(";")[0].trim();
            const [currentState, currentSymbol, newSymbol, direction, newState] = lineWithoutComments.split(" ");
            return { currentState, currentSymbol, newSymbol, direction, newState };
        });

    return filteredLines;
}

function turningMachine(rulesFilePath, rules, input) {
    const tape = (input.replace(" ", "_").split(""));
    let currentState = "0";
    let tapePosition = 0;
    while (true) {
        const currentSymbol = tape[tapePosition];
        const selectedRule = findRule(currentState, currentSymbol, rules);
        const stateAndSymbolCombinationNotFound = selectedRule === null;
        if (stateAndSymbolCombinationNotFound) {
            console.log(`${rulesFilePath},${input},ERR`);
            return;
        }
        const symbolNeedsToBeReplaced = selectedRule.newSymbol !== "*";
        if (symbolNeedsToBeReplaced) {
            tape[tapePosition] = selectedRule.newSymbol;
        }
        if (selectedRule.newState.startsWith("halt")) {
            console.log(`${rulesFilePath},${input},${tape.join("").replace(/_/g, " ").trim()}`);
            return;
        }
        if (selectedRule.direction === "r") {
            tapePosition++;
            if (tapePosition >= tape.length) {
                tape.push("_");
            }
        } else if (selectedRule.direction === "l") {
            tapePosition--;
            if (tapePosition < 0) {
                tape.unshift("_");
                tapePosition = 0;
            }
        }
        currentState = selectedRule.newState;
    }
}

function findRule(state, symbol, rules) {
    for (let i = 0; i < rules.length; i++) {
        if (rules[i].currentState === state && rules[i].currentSymbol === symbol) {
            return { ...rules[i] };
        }
    }

    for (let i = 0; i < rules.length; i++) {
        if ((rules[i].currentState === state || rules[i].currentState === "*") && (rules[i].currentSymbol === symbol || rules[i].currentSymbol === "*")) {
            return { ...rules[i] };
        }
    }

    return null;
}

const filename = process.argv[2];

if (!filename) {
    console.log("Nenhum argumento foi passado.");
    console.log("Exemplo de uso: node turing.js datafile");
    process.exit(1);
}

processFile(filename);
