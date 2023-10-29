
function soma(valor1, valor2) {
    return valor1 + valor2;
}

function realParaDolar(real, cotacaoDolar) {
    return real * cotacaoDolar;
}

var valorReal = 8.89;
var cotacao = 5.08;

var total = realParaDolar(valorReal, cotacao);


function alertaHello() {
    alert("o valor em real é R$: "+valorReal+"  o valor em dólar é u$ é: " +total)
    document.body.style.backgroundColor = "yellow";

}




function paraCelsius(valorFahrenheit) {
    return (5 / 9) * (valorFahrenheit - 32);
}


var x = paraCelsius(77);

alert( "A Temperatura é de " + x + " graus celsius" );



function minhaFuncao() {
    var x = 2;
}

 function viraVermelho() {
    document.body.style.backgroundColor = "red";


 }

 function limpaTexto() {
    document.getElementById("campoFocado").value = "";
 }

 const lista = ["arroz", "feijao" , "manteiga" , "leite"]
 alert(lista);

 const ola = ["arroz", "feijao" , "manteiga" , "leite"];

 alert(Array.isArray(ola));


 console.log(micro)