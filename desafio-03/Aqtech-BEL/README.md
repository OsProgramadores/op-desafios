  <h1>README - Filtro de Números Palíndromos</h1>

  <h2>🔍 Objetivo</h2>
  <p>
    O objetivo deste código foi filtrar um array de números e retornar apenas aqueles que são <strong>palíndromos</strong>, ou seja, números que continuam iguais mesmo se lidos de trás para frente (como <code>121</code>, <code>44</code>, <code>1331</code>).
  </p>

  <h2>👨‍💻 Minha Primeira Tentativa</h2>
  <p>
    A ideia inicial era usar o <code>%</code> para pegar o resto da divisão por 10 e, a partir disso, montar o número invertido multiplicando os dígitos e acumulando até formar o número completo de trás pra frente. Depois, minha intenção era comparar esse número invertido com o número original pra saber se era palíndromo.
  </p>
  <p>
    Apesar de a ideia estar no caminho certo, cometi alguns erros na execução:
  </p>

  <div class="highlight">
    <strong>Erros que cometi:</strong>
    <ul>
      <li>Coloquei um <code>for</code> dentro do <code>filter()</code>, sendo que ele já percorre o array.</li>
      <li>Fiz a extração de apenas um dígito fora do <code>while</code>, sem atualizar o valor dentro do loop.</li>
      <li>Não atualizei corretamente o número original, o que fez com que o laço <code>while</code> não funcionasse como esperado.</li>
      <li>Usei <code>console.log()</code> dentro do <code>filter()</code> ao invés de retornar <code>true</code> ou <code>false</code>.</li>
    </ul>
  </div>

  <h2>✅ Código Corrigido</h2>
  <p>
    Depois que entendi melhor como o <code>filter()</code> funciona e como manipular os dígitos corretamente, reescrevi o código da forma correta. Agora uso um <code>while</code> para pegar cada dígito do número com <code>% 10</code>, monto o número invertido multiplicando por 10 e somando o dígito, e atualizo o número original com <code>Math.floor(num / 10)</code> para remover a parte decimal.
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
    <li>Aprendi que o <code>filter()</code> já percorre o array e não precisa de um <code>for</code> interno.</li>
    <li>Compreendi como inverter um número matematicamente, pegando os dígitos com <code>%</code> e usando <code>Math.floor()</code> para remover a parte decimal.</li>
    <li>Entendi que é essencial retornar um valor booleano dentro do <code>filter()</code>, e não apenas imprimir no console.</li>
    <li>Aprendi que cada passo da lógica precisa ser bem planejado, principalmente quando se trata de manipulação numérica.</li>
    <li>Percebi como pequenos detalhes, como atualizar o número dentro do <code>while</code>, fazem toda a diferença.</li>
  </ul>

  <h2>📦 Por que usei <code>Math.floor()</code></h2>
  <p>
    Usei <code>Math.floor()</code> porque, ao inverter o número, eu precisava ir removendo os dígitos da direita. Ao dividir por 10 em JavaScript, o resultado pode ser um número com casas decimais (como <code>123 / 10 = 12.3</code>). Isso causaria problemas no laço <code>while</code>, que nunca terminaria corretamente. Com o <code>Math.floor()</code>, eu consegui simular uma divisão inteira, que descarta os decimais e permite que o processo de inversão funcione corretamente.
  </p>
