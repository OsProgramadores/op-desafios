function listaPrimos(num) {
	if (num < 2) {
		return false
	}
	for (let i = 2; i < num; i++) {
		if (num % i === 0) {
			return false
		}
	}
	return true
}

let numero = []
for (let i = 0; i < 10000; i++) {
	numero[i] = i + 1
}

var resultado = numero.filter(listaPrimos)

console.log(`Os números primos de 1 a 10000 são:\n ${resultado}.`)
