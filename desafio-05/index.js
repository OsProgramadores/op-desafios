function main(){
    const dados = require('./funcionarios.json');


    function salarioGeral(){

        let salarioMaior = -Infinity;
        let salarioMenor = Infinity;
        let salarioMedia = 0;
        let salarioCont = 0;
        let nomeMaior = [];
        let nomeMenor = [];

        // rodando a cada funcionario
        dados.funcionarios.forEach(func => {

            // salario maior
            if(func.salario > salarioMaior){
                salarioMaior = func.salario;
                nomeMaior = [`${func.nome} ${func.sobrenome}`];
            }else if(func.salario == salarioMaior){
                nomeMaior.push(`${func.nome} ${func.sobrenome}`);
            }

            // salario menor
            if(func.salario < salarioMenor){
                salarioMenor = func.salario;
                nomeMenor = [`${func.nome} ${func.sobrenome}`];   
            }else if(func.salario == salarioMenor){
                nomeMenor.push(`${func.nome} ${func.sobrenome}`);
            }

            salarioMedia += func.salario
            salarioCont++
        });
        
        const mediaSalario = salarioMedia/salarioCont;

        console.log("<-===================================================->")
        console.log("Maior salário é do", nomeMaior.join(", "), "de:", salarioMaior);
        console.log("Menor salário é do", nomeMenor.join(", "), "de:", salarioMenor);  
        console.log("A media de salários é de:", mediaSalario.toFixed(2));  
        console.log("<-===================================================->")

    }

    function salarioArea(){
        
        let salarioMaiorArea_SD = -Infinity;
        let salarioMenorArea_SD = Infinity;
        let salarioMediaArea_SD = 0;
        let salarioContArea_SD = 0;
        let nomeMaiorArea_SD = [];
        let nomeMenorArea_SD = [];       

        let salarioMaiorArea_SM = -Infinity;
        let salarioMenorArea_SM = Infinity;
        let salarioMediaArea_SM = 0;
        let salarioContArea_SM = 0;
        let nomeMaiorArea_SM = [];
        let nomeMenorArea_SM = [];    

        let salarioMaiorArea_UD = -Infinity;
        let salarioMenorArea_UD = Infinity;
        let salarioMediaArea_UD = 0;
        let salarioContArea_UD = 0;
        let nomeMaiorArea_UD = [];
        let nomeMenorArea_UD = [];       

        // rodando a cada funcionario
        dados.funcionarios.forEach(func => {
        
        //area SM 
        if(func.area === "SM"){    

            // salario maior SM
            if(func.salario > salarioMaiorArea_SM){
                salarioMaiorArea_SM = func.salario;
                nomeMaiorArea_SM = [`${func.nome} ${func.sobrenome}`];
            }else if(func.salario == salarioMaiorArea_SM){
                nomeMaiorArea_SM.push(`${func.nome} ${func.sobrenome}`);
            }

            // salario menor SD
            if(func.salario < salarioMenorArea_SM){
                salarioMenorArea_SM = func.salario;
                nomeMenorArea_SM = [`${func.nome} ${func.sobrenome}`];   
            }else if(func.salario == salarioMenorArea_SM){
                nomeMenorArea_SM.push(`${func.nome} ${func.sobrenome}`);
            }

            salarioMediaArea_SM += func.salario;
            salarioContArea_SM++
        }

        //area UD
        if(func.area === "UD"){    

            // salario maior UD
            if(func.salario > salarioMaiorArea_UD){
                salarioMaiorArea_UD = func.salario;
                nomeMaiorArea_UD = [`${func.nome} ${func.sobrenome}`];
            }else if(func.salario == salarioMaiorArea_UD){
                nomeMaiorArea_UD.push(`${func.nome} ${func.sobrenome}`);
            }

            // salario menor UD
            if(func.salario < salarioMenorArea_UD){
                salarioMenorArea_UD = func.salario;
                nomeMenorArea_UD = [`${func.nome} ${func.sobrenome}`];   
            }else if(func.salario == salarioMenorArea_UD){
                nomeMenorArea_UD.push(`${func.nome} ${func.sobrenome}`);
            }

            salarioMediaArea_UD += func.salario;
            salarioContArea_UD++
        }

        //area SD 
        if(func.area === "SD"){    

            // salario maior SD
            if(func.salario > salarioMaiorArea_SD){
                salarioMaiorArea_SD = func.salario;
                nomeMaiorArea_SD = [`${func.nome} ${func.sobrenome}`];
            }else if(func.salario == salarioMaiorArea_SD){
                nomeMaiorArea_SD.push(`${func.nome} ${func.sobrenome}`);
            }

            // salario menor SD
            if(func.salario < salarioMenorArea_SD){
                salarioMenorArea_SD = func.salario;
                nomeMenorArea_SD = [`${func.nome} ${func.sobrenome}`];   
            }else if(func.salario == salarioMenorArea_SD){
                nomeMenorArea_SD.push(`${func.nome} ${func.sobrenome}`);
            }

            salarioMediaArea_SD += func.salario;
            salarioContArea_SD++
        }

        // fim do loop por pessoa
        })
        const mediaSalarioArea_SD = (salarioMediaArea_SD / salarioContArea_SD);
        const mediaSalarioArea_UD = (salarioMediaArea_UD / salarioContArea_UD);        
        const mediaSalarioArea_SM = (salarioMediaArea_SM / salarioContArea_SM);
        
        console.log("<-===================================================->")
        console.log("Na área SD ->");
        console.log("Maior salário é do", nomeMaiorArea_SD.join(", "), "de:", salarioMaiorArea_SD);
        console.log("Menor salário é do", nomeMenorArea_SD.join(", "), "de:", salarioMenorArea_SD);  
        console.log("A media de salários é de:", mediaSalarioArea_SD.toFixed(2)); 
        console.log("-------------------------------------------------------");
        console.log("Na área SM ->");
        console.log("Maior salário é do", nomeMaiorArea_SM.join(", "), "de:", salarioMaiorArea_SM);
        console.log("Menor salário é do", nomeMenorArea_SM.join(", "), "de:", salarioMenorArea_SM);  
        console.log("A media de salários é de:", mediaSalarioArea_SM.toFixed(2));        
        console.log("-------------------------------------------------------");
        console.log("Na área UD ->");
        console.log("Maior salário é do", nomeMaiorArea_UD.join(", "), "de:", salarioMaiorArea_UD);
        console.log("Menor salário é do", nomeMenorArea_UD.join(", "), "de:", salarioMenorArea_UD);  
        console.log("A media de salários é de:", mediaSalarioArea_UD.toFixed(2));
        console.log("<-===================================================->")

    }

    function areasFuncionarios(){

        let area_SM = 0;
        let area_UD = 0;
        let area_SD = 0;
        
        dados.funcionarios.forEach(func => {

            if(func.area == "SM"){
                area_SM++;
            }
            if(func.area == "UD"){
                area_UD++;
            }
            if(func.area == "SD"){
                area_SD++;
            }

        })

        console.log("<-===================================================->")
        console.log(`Na area SD tem: ${area_SD}`);
        console.log(`Na area SM tem: ${area_SM}`);
        console.log(`Na area UD tem: ${area_UD}`);        
        console.log("<-===================================================->")

    }

    function salarioSobrenome(){

        const sobrenomes = {};

        // agrupar funcionários por sobrenome
        dados.funcionarios.forEach(func => {
            if(!sobrenomes[func.sobrenome]){
                sobrenomes[func.sobrenome] = [];
            }
            sobrenomes[func.sobrenome].push(func);
        });
        
        for(let sobrenome in sobrenomes){
            
            const grupo = sobrenomes[sobrenome];
            if(grupo.length > 1){

                let maiorSalario = -Infinity;
                let maiores = [];
    
                grupo.forEach(func => {
                    if(func.salario > maiorSalario){
                        maiorSalario = func.salario;
                        maiores = [
                            `${func.nome} ${func.sobrenome}`
                        ];
                    }
                    
                    else if(func.salario == maiorSalario){

                        maiores.push(
                            `${func.nome} ${func.sobrenome}`
                        );

                    }

                });

                console.log(
                    `${sobrenome}: ${maiores.join(", ")} - ${maiorSalario}`
                );

            }

        }

    }

    salarioGeral();
    salarioArea();
    areasFuncionarios();
    console.log("<-===================================================->");
    salarioSobrenome();
    console.log("<-===================================================->");
}
main();