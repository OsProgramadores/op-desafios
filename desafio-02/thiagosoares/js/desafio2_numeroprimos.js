for(let i = 2; i <= 10000; i++){
  let nPrimo = true;
    for(let j = 2; j < i; j++){
       if(i % j === 0){
         nPrimo = false;
         break;
       }
    }
  if(nPrimo){
      console.log(i);
  }
}
