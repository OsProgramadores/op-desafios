function primo() {
    
    //var i para os números que serão checados se são primos ou não
    var i = 0;
    
    //var x para que haja a divisão entre i e x para averiguar o modal entre elas
    var x = 0;
    
    //var divisor que será a soma de divisores totais entre os número i e número x
    var divisor = 0;
  
    for (i = 2; i <= 10000; i++) {
      
      //toda vez que o for loop começar e se e rodar novamente, devemos resetar a variável divisor
      //para que ela não se acumule
      divisor = 0;
      
      //a utilização do número x irá checar a quantidade de divisores entre a divisão i e x
      //note que o for loop aqui irá realizar a divisão de todos os números x que começará do 1
      //até chegar no número i
      for (x = 1; x <= i; x++) {
        
        //aqui checaremos se o modal entre i e x é zero
        //caso seja zero, o número de divisores irá ser acrescido
        
        if (i % x == 0) {
          divisor =+ 1;
        }
      
      }
      //números primos só são divisíveis por 1 e por eles mesmos, portanto
      //se o número de divisores for no total 2, o número é primo, e o código irá retornar o valor
      //por fim, o divisor será resetado no início do código, para que seja feita a verificação novamente
      if (divisor == 2) {
        console.log(i);
      }
    }
  }
  
  primo();
  
  