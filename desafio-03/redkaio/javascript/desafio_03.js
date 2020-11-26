//Aqui a função irá receber os valores inicial e final para o começar a rodar
function palindromo (x, y) {
    let i;
    //Antes de qualquer coisa, iremos verificar se x for maior que y, para que o
    //programa retorne os valores de forma decrescente. Caso contrário, irá
    //retornar os valores em ordem crescente
    if (x > y) {
        for (i = x; i > y; i--) {
            //Utilizando funcões que irão realizar tarefas específicas e alocá-las na variável:
            //toString irá transformar o número em uma string
            //split('') irá dividir os números e colocá-los em um array
            //reverse() irá inverter as posições do array
            //join('') irá juntar novamente os caracteres que foram invertidos
            isPalyndrome = i.toString().split('').reverse().join('');
            //Por fim, se o número i for igual a variável,
            //irá retornar o número palíndrimo
            if (isPalyndrome == i) {
                console.log(i);
            }
        }
    } else {
        for (i = x; i <= y; i++) {
            isPalyndrome = i.toString().split('').reverse().join('');
            if (isPalyndrome == i) {
                console.log(i);
            }
        }
    }
}
palindromo(100000,3003000);