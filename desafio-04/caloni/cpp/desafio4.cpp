#include <iostream>

using namespace std;

int main()
{
    const char *pieceNames[7] = { "Vazio", "Peão", "Bispo", "Cavalo", "Torre", "Rainha", "Rei" };
    int pieceCounts[7] = {};
    for( int i = 0; i < 64; ++i )
    {
        int idx = 0;
        cin >> idx;
        ++pieceCounts[idx];
    }
    for( int i = 1; i < 7; ++i )
        cout << pieceNames[i] << ": " << pieceCounts[i] << " peça(s)\n";
}

