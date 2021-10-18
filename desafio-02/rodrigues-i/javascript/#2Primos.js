// Imprime no console todos os números primos entre 1 e 10.000
const numerosPrimos = () => {
	
	let nãoPrimos = [];
	let primos = [];
	let contagem = 0;

	for(let i = 2; i <= 10000; i++) {
		if(primos.length >= 1) {
			for(item of primos) {
				if(i % item === 0) {
					continue;
				}
			}	
		}
		for(let j = 1; j <= i; j++) {
			if(i % j === 0) {
				contagem++;
				if(contagem > 2){
					nãoPrimos.push(i);
					contagem = 0;
					break;
				}
			if(i % j === 0 && j === i) {
				primos.push(i);
				console.log(i);
				contagem = 0;
				break;
				}
			}
		}
	}			
};

numerosPrimos();