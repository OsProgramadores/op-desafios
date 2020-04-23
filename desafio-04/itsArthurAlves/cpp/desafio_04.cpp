#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

void entertab(int x[][8]){
  int i, j, w = 9;
  char z;
  for (i=0; i<8; i++){
    w--;
    for(j=0; j<8; j++){
      z = (j==0) ? ('A') :
          (j==1) ? ('B') :
          (j==2) ? ('C') :
          (j==3) ? ('D') :
          (j==4) ? ('E') :
          (j==5) ? ('F') :
          (j==6) ? ('G') :
          (j==7) ? ('H') : ('I');
      cout<<"Vazio: 0\nPeão: 1\nBispo: 2\nCavalo: 3\nTorre: 4\nRainha: 5\nRei: 6\n";
      cout<<"["<<w<<"]"<<"["<<z<<"]"<<" ? : ";
      cin>>x[i][j];
      system("clear");
    };
  }
};

void outtab(int x[][8]){
 int i, j, z, peao = 0, bispo = 0, cavalo = 0, torre = 0, rainha = 0, rei = 0, vazio = 0;
 for(i=0; i<8; i++){
  z = (i==0) ? (8) :
      (i==1) ? (7) :
      (i==2) ? (6) :
      (i==3) ? (5) :
      (i==4) ? (4) :
      (i==5) ? (3) :
      (i==6) ? (2) :
      (i==7) ? (1) : (9);
  cout<<z<<" > ";
  for(j=0;j<8; j++){
     cout<<x[i][j]<<" ";
     vazio = (x[i][j] == 0) ? (vazio+1) : (vazio);
     peao = (x[i][j] == 1) ? (peao+1) : (peao);
     bispo = (x[i][j] == 2) ? (bispo+1) : (bispo);
     cavalo = (x[i][j] == 3) ? (cavalo+1) : (cavalo);
     torre = (x[i][j] == 4) ? (torre+1) : (torre);
     rainha = (x[i][j] == 5) ? (rainha+1) : (rainha);
     rei = (x[i][j] == 6) ? (rei+1) : (rei);
  };
  cout<<"\n";
 };
 cout<<"    ^ ^ ^ ^ ^ ^ ^ ^ \n";
 cout<<"    A B C D E F G H \n";
 cout<<"\nVazio: "<<vazio<<" peça(s)"<<"\nPeão: "<<peao<<" peça(s)\n"<<"Bispo: "<<bispo<<" peça(s)\n"<<"Cavalo: "<<cavalo<<" peça(s)\n";
 cout<<"Torre: "<<torre<<" peça(s)\n"<<"Rainha: "<<rainha<<" peça(s)\n"<<"Rei: "<<rei<<" peça(s)\n";
};

int main(){
  int i, j, matrix[8][8];
  entertab(matrix);
  outtab(matrix);
return(0);
 
}