"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.TuringMachine = void 0;
class TuringMachine {
    read() {
        this.cpu.symbol = this.tape[this.cpu.tapePosition];
    }
    write(symbol) {
        if (symbol !== '*') {
            this.tape[this.cpu.tapePosition] = symbol === '_' ? ' ' : symbol;
        }
    }
    moveRight() {
        this.cpu.tapePosition += 1;
        if (this.cpu.tapePosition >= this.tape.length) {
            this.tape.push(' ');
        }
    }
    moveLeft() {
        if (this.cpu.tapePosition <= 0) {
            this.tape.unshift(' ');
        }
        else {
            this.cpu.tapePosition -= 1;
        }
    }
    moveHead(direction) {
        switch (direction) {
            case 'l':
                this.moveLeft();
                break;
            case 'r':
                this.moveRight();
                break;
            case '*':
                return;
            default:
                throw new Error(`invalid direction: ${direction}`);
        }
    }
    findRule(state, symbol) {
        let matchingRule = this.rules.find(rule => rule.state === state && rule.symbol === symbol);
        if (!matchingRule) {
            matchingRule = this.rules.find(rule => {
                const stateMatches = rule.state === state || state === '*';
                const symbolMatches = rule.symbol === symbol || symbol === '*' || rule.symbol === '*';
                return ((rule.state === state && (symbol === '*' || rule.symbol === '*')) ||
                    (rule.state === '*' && rule.symbol === symbol));
            });
        }
        if (!matchingRule) {
            throw new Error(`Rule not found: state:${state} symbol:${symbol}`);
        }
        return matchingRule;
    }
    loadRules(rulesFile) {
        const ruleLines = rulesFile
            .split(/\r\n|\n/)
            // clear comments and blank lines
            .filter(line => !line.trim().startsWith(';') && line);
        this.rules = ruleLines.map((line, index) => {
            const ruleLine = line.split(' ');
            if (ruleLine.length < 5) {
                throw new Error(`invalid rule at line ${index}:${ruleLine}`);
            }
            return {
                state: ruleLine[0],
                symbol: ruleLine[1],
                newSymbol: ruleLine[2],
                direction: ruleLine[3],
                newState: ruleLine[4],
            };
        });
        // console.log(this.rules);
    }
    reset() {
        this.cpu = {
            state: '0',
            symbol: '',
            tapePosition: 0,
        };
    }
    loadTape(tape) {
        this.tape = tape.split('');
    }
    step() {
        this.cpu.symbol = this.tape[this.cpu.tapePosition];
        // console.log(this.cpu);
        // console.log(this.tape);
        if (this.cpu.symbol === ' ')
            this.cpu.symbol = '_';
        if (!this.cpu.symbol)
            throw new Error('symbol undefined');
        const rule = this.findRule(this.cpu.state, this.cpu.symbol);
        // console.log(rule);
        this.cpu.state = rule.newState;
        this.write(rule.newSymbol);
        this.moveHead(rule.direction);
    }
    run() {
        while (!this.cpu.state.startsWith('halt')) {
            this.step();
        }
        return this.tape.join('');
    }
}
exports.TuringMachine = TuringMachine;
