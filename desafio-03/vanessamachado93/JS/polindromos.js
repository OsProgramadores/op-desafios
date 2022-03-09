function varificaPolindromos(number) {
	if (number < 10) return true
	const array = number.toString().split('')
	const reverse = array.reverse().join('')
	return number === Number(reverse)
}

function pegaPolindromosEntre(a, b) {
	const numbers = []

	if (a < 0 || b < 0 || a > b) return numbers

	for (let i = a; i <= b; i++) if (varificaPolindromos(i)) numbers.push(i)

	return numbers
}

console.log(pegaPolindromosEntre(1001, 4001))
