function getPrime(valor){
    let result = "";  
    for(let counter = 1; counter <= valor; counter++){
        let divisor = 0;
        for(let aux = 1 ; aux <= counter ; aux++){
            if(counter % aux === 0){
                divisor++;
            }  
        }
        if(divisor === 2){
            result += `${counter}, `;
        }
    }
    console.log(result);
}
getPrime(1000);