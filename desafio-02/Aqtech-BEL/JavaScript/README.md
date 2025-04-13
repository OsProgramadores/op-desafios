<h1>Desafio 02 - Os Programadores</h1>
<p><strong>Autor:</strong> Aqtech-BEL</p>
<p><strong>Proposto por:</strong> <a href="https://github.com/OsProgramadores" target="_blank">Os Programadores</a></p>

<h2>📌 Descrição</h2>
<p>Este desafio consiste em identificar e listar todos os números primos entre 1 e 10.000. O algoritmo percorre um intervalo de números e utiliza uma função de filtragem para determinar se cada número é primo, com base na quantidade de divisores inteiros positivos.</p>

<h2>🧠 Lógica utilizada</h2>
<p>Um número é considerado primo se for maior que 1 e tiver exatamente dois divisores: 1 e ele mesmo. O algoritmo percorre o intervalo de 1 a 10.000, testa cada número e conta quantos divisores ele possui. Se tiver apenas dois divisores, ele é considerado primo e incluído na lista de saída.</p>

<p><strong>Alterações realizadas no código:</strong></p>
<ol>
    <li><strong>O uso de `Math.sqrt(num)`:</strong> Inicialmente, o código testava todos os divisores de 1 até o próprio número. A alteração foi feita para otimizar o processo, utilizando a raiz quadrada do número para limitar os divisores a serem testados até a raiz quadrada de `num`. Isso melhora a performance do código.</li>
    <li><strong>Começar o loop em 2:</strong> O loop agora começa a verificação de divisores a partir de 2, pois números menores que 2 (como 0 e 1) não são primos. Antes, o código testava também o número 1, o que não é necessário.</li>
    <li><strong>Saída do código:</strong> O código agora é mais eficiente e rápido, especialmente ao lidar com grandes números, devido à redução da quantidade de divisões feitas.</li>
</ol>

<h2>🛠️ Como usar</h2>
<ol>
    <li>Certifique-se de ter o Node.js instalado. Se não tiver, pode baixá-lo no site oficial: <a href="https://nodejs.org" target="_blank">https://nodejs.org</a>.</li>
    <li>Salve o código JavaScript em um arquivo (por exemplo: <code>desafio02.js</code>).</li>
    <li>Abra o terminal (ou prompt de comando) e navegue até a pasta onde o arquivo foi salvo.</li>
    <li>Execute o arquivo usando o seguinte comando:</li>
</ol>
<pre><code>node desafio02.js</code></pre>
<p>O programa imprimirá no console todos os números primos entre 1 e 10.000.</p>

<h2>✅ Exemplo de saída</h2>
<pre><code>[2, 3, 5, 7, 11, 13, 17, ... 9973]</code></pre>

<h2>📈 Melhorias e Performance</h2>
<p>As melhorias feitas no código resultam em uma execução mais rápida e eficiente. Ao testar divisores apenas até a raiz quadrada do número, o número de operações é reduzido consideravelmente. Por exemplo, ao verificar se um número como 10.000 é primo, o código só precisa realizar verificações até cerca de 100 (a raiz quadrada de 10.000), ao invés de testar até 10.000 divisores. Isso acelera significativamente o tempo de execução, especialmente para grandes intervalos de números.</p>

<h2>🔧 Código otimizado</h2>
<pre><code>
const cousinNumber = numbers.filter((num) => {
    if (num < 2) {
        return false; // Números menores que 2 não são primos
    }

    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
        return false; // Se achar um divisor, o número não é primo
    }

    return true; // Caso contrário, o número é primo
});
</code></pre>

<p>Essa versão otimizada reduz o número de iterações necessárias e torna o código mais eficiente, especialmente quando lidamos com números maiores.</p>
