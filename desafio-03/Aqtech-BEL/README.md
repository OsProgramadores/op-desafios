  <h1>Desafio-03 - Números Palíndromos</h1>

  <h2>🔍 Objetivo</h2>
  <p>
    O objetivo deste código foi criar uma forma de percorrer um array de números e retornar apenas aqueles que são <strong>palíndromos</strong>, ou seja, números que continuam iguais mesmo se lidos de trás para frente (como <code>121</code>, <code>44</code>, <code>1331</code>).
  </p>

  <h2>📌 Meu Primeiro Código</h2>
  <p>
    Quando comecei, tentei criar a lógica por conta própria, usando um <code>for</code> dentro de um <code>filter()</code> e fazendo algumas divisões por 10 para "quebrar" o número. Achei que isso seria suficiente para saber se o número era palíndromo. Mas não funcionou como eu esperava.
  </p>

  <div class="highlight">
    <strong>Erros que cometi:</strong>
    <ul>
      <li>Usei um <code>for</code> desnecessariamente dentro do <code>filter()</code>, mesmo ele já percorrendo o array.</li>
      <li>Tentei descobrir se um número era palíndromo apenas dividindo ele por 10, o que não faz sentido.</li>
      <li>Calculei apenas um dígito fora do <code>while</code> e usei ele repetidamente, sem atualizá-lo.</li>
      <li>Usei <code>console.log()</code> dentro do <code>filter()</code> ao invés de retornar <code>true</code> ou <code>false</code>.</li>
    </ul>
  </div>

  <h2>✅ Código Corrigido</h2>
  <p>
    Depois de entender melhor o problema, reescrevi a lógica e consegui corrigir tudo. O código final ficou assim:
  </p>

  <pre><code>
const numbers = [121, 123, 44, 1331, 789];

const palindromicos = numbers.filter((num) => {
  let original = num;
  let reversed = 0;

  while (num > 0) {
    let digit = num % 10;
    reversed = reversed * 10 + digit;
    num = Math.floor(num / 10);
  }

  return original === reversed;
});

console.log(palindromicos); // Saída: [121, 44, 1331]
  </code></pre>

  <h2>📚 O que eu aprendi</h2>
  <ul>
    <li>Aprendi que o <code>filter()</code> já percorre o array, então não preciso usar um <code>for</code> dentro dele.</li>
    <li>Entendi como inverter um número de forma matemática usando <code>while</code>, <code>%</code> e <code>Math.floor()</code>.</li>
    <li>Descobri que dentro do <code>filter()</code> eu preciso retornar <code>true</code> ou <code>false</code> — e não apenas imprimir algo no console.</li>
    <li>Aprendi a importância de atualizar as variáveis corretamente dentro de um loop.</li>
    <li>Agora sei comparar o número original com o invertido para verificar se ele é realmente palíndromo.</li>
  </ul>

  <h2>📦 Por que usei <code>Math.floor()</code></h2>
  <p>
    Eu usei <code>Math.floor()</code> porque durante o processo de inverter o número, eu precisava ir "apagando" os últimos dígitos, dividindo o número por 10 a cada repetição.
  </p>
  <p>
    Mas dividir por 10 em JavaScript não dá um número inteiro. Por exemplo, <code>123 / 10</code> dá <code>12.3</code>. Eu precisava de <code>12</code>, então foi aí que usei <code>Math.floor()</code>, que serve justamente para <strong>arredondar o número para baixo</strong>.
  </p>
  <p>
    Sem ele, meu loop nunca chegaria a zero, e o processo de inversão daria errado.
  </p>

  <h2>💡 Minha Reflexão</h2>
  <p>
    Esse exercício me ensinou que a lógica é mais importante do que sair tentando código aleatoriamente. Cometi erros simples que me mostraram o valor de entender cada função, especialmente em JavaScript. Foi legal ver que, ao entender o problema com calma, consegui construir a solução e aprender algo novo sobre matemática e programação ao mesmo tempo.
  </p>
