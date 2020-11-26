for (var i = 2; i <= 10000; i++)
{
	printPrimes(i)
}
function printPrimes(input_number)
{
	let divisores = 0;
	for (var i = 2; i <= input_number; i++)
	{
		if (input_number % i == 0) divisores++
	}
	if (divisores === 1) console.log(input_number);
}