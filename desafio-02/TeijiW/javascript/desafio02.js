for(let n=1;n<=10000;n++){
    count = 0
    for (let i=1;i<=n;i++){
       if (n%i === 0){
         count++
       } 
    }
    if (count === 2){
      console.log(n)
    }
  }