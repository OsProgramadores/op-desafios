for (var i = 1; i <= 10000; i++) {
	imprimePrimos(i)
}
function imprimePrimos(input_number){
	let divisores = 0;
	for (var i = 1; i <= input_number; i++) {
	if (input_number % i == 0){
		divisores++
	}
	}
	if (divisores == 2) {console.log(input_number)}}
