for(var i=1; i<= 100000; i++)
{
  var eh_palidromo = true;
  var string = String(i).split("");
  
  for(var j=0; j<string.length/2; j++){
      if(string[j] != string[string.length-(1+j)]){
        eh_palidromo = false;
        break;
      }
  }
  
  if(eh_palidromo)
    console.log(i);
}
