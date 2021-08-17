/*Tabuleiro (vetor) de xadrez com peças na posição inicial do jogo*/

var tabuleiro = [4,3,2,5,6,2,3,4,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,4,3,2,5,6,2,3,4];

/*
console.log(tabuleiro); *O log do tabuleiro está comentado mas pode ser retirado para visualização do vetor.
*/

/*Peão - 1*/

function peao(value) {
  return value == 1;
}
var pecap = tabuleiro.filter(peao);
var peaolength = pecap.length;
console.log("Peão: " + peaolength + " peças");

/*Bispo - 2*/

function bispo(value) {
  return value == 2;
}
var pecab = tabuleiro.filter(bispo);
var bispolength = pecab.length;
console.log("Bispo: " + bispolength + " peças");

/*Cavalo - 3*/

function cavalo(value) {
  return value == 3;
}
var pecac = tabuleiro.filter(cavalo);
var cavalolength = pecac.length;
console.log("Cavalo: " + cavalolength + " peças");

/*Torre - 4*/

function torre(value) {
  return value == 4;
}
var pecat = tabuleiro.filter(torre);
var torrelength = pecat.length;
console.log("Torre: " + torrelength + " peças");

/*Rainha - 5*/

function rainha(value) {
  return value == 5;
}
var pecara = tabuleiro.filter(rainha);
var rainhalength = pecara.length;
console.log("Rainha: " + rainhalength + " peças");

/*Rei - 6*/

function rei(value) {
  return value == 6;
}
var pecare = tabuleiro.filter(rei);
var reilength = pecare.length;
console.log("Rei: " + reilength + " peças");