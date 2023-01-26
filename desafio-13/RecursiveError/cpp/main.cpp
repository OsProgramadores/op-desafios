/*
Solução desafio-13
Author: Guilherme Silva Schultz
Data: 26/01/2023

minha solução para esse desafio era com um algoritmo de brute-force
apesar de gerar a resposta correta, é extremamente demorado
um campo de 8x8 tem trilhões de trilhões de posibilidades

então fui pesquisar sobre algoritmo mais eficientes
com um pouco de pesquisa descobrir a Warnsdorff's rule
essa é uma regra heuristica, que diz
se proximo movimento sempre for para posição com a menor possibilidades de proximos movimentos
as chances de achar a resposta é alta

assim cheguei neste resultado:
*/

#include <array>
#include <iostream>
#include <map>
#include <string>
#include <vector>

//estado das casas do campo
enum PointState { Occupied, Open };

//estado do caminho
enum PathState  { Error, Ok };

//estrutura para pontos no plano 2D
struct Point_2D {
    int x{0};
    int y{0};
    Point_2D(int _x, int _y) : x{_x}, y{_y}{}
};

//estrutura do campo
struct Chess_board {
  Chess_board(std::map<std::string, PointState> m,
              std::array<std::array<std::string, 8>, 8> a) :
    board_map{m}, board_array{a}
    {}
    std::string operator[](Point_2D point){
        return this->board_array[point.x][point.y];
    }
    PointState operator[](std::string point){
        return this->board_map[point];
    }

    std::map<std::string, PointState> board_map{};
    std::array<std::array<std::string, 8>, 8> board_array{};
};

//movimentos do cavalo
const auto moves_array = std::array<Point_2D,8>{Point_2D(1, 2), Point_2D(-1, 2),
                        Point_2D(-2, 1), Point_2D(-2, -1),
                        Point_2D(-1, -2), Point_2D(1, -2),
                        Point_2D(2, -1), Point_2D(2, 1)
};


//criar um array 8x8 com coordenadas do tabuleiro
std::array<std::array<std::string, 8>, 8> gen_board() {
  auto arr = {"a", "b", "c", "d", "e", "f", "g", "h"};
  std::array<std::array<std::string, 8>, 8> board{};
  std::array<std::string, 8> buff{};
  int array_index = 0;
  for (auto l : arr) {
    for (int i = 0; i < 8; i++) {
      buff[i] = l + std::to_string(i + 1);
    }
    board[array_index] = buff;
    array_index++;
  }
  return board;
}

//cria um mapa do tabuleiro
std::map<std::string, PointState> gen_map(std::string begin, std::array<std::array<std::string, 8>, 8> &board) {
    auto chess_map = std::map<std::string, PointState>();
    for (auto line : board) {
        for (auto row : line) {
            chess_map[row] = PointState::Open;
        }
    }
    chess_map[begin] = PointState::Occupied;
    return chess_map;
}

//retorna true se o estado do ponto for Open
bool check_point(Point_2D point, Chess_board &board){
    return board[board[point]] == PointState::Open;
}

//gera todos os possiveis movimentos a partir de uma coordenada x,y
std::vector<Point_2D> gen_moves(Point_2D begin, Chess_board &board) {
    std::vector<Point_2D> moves;
    int x = 0;
    int y = 0;
    for(auto m : moves_array){
        x = begin.x + m.x;
        y = begin.y + m.y;
        if((x <= 7 && x >= 0) && (y <= 7 && y >= 0)){
            switch(board[board.board_array[x][y]]){
                case PointState::Open:
                    moves.push_back(Point_2D(x, y));
                    break;
                case PointState::Occupied:
                    break;
            };
        }
    }
    return moves;
}

//aplica Warnsdorff's rule e retorna o proximo passo
Point_2D gen_close_path(std::vector<Point_2D> &moves, Chess_board &board){
    auto v_size = gen_moves(moves[0], board).size();
    Point_2D v_point(0,0);
    std::vector<Point_2D> close_path;
    for(auto move : moves){
        close_path = gen_moves(move, board);
        if(v_size >= close_path.size()){
            if(check_point(move, board)){
                v_size = close_path.size();
                v_point = move;
            }
        }
    }
    return v_point;
}

//gera a solução recursivamente
PathState gen_path(Point_2D point, Chess_board &board, int rows_left ,std::vector<Point_2D> &result){
    std::vector<Point_2D> moves = gen_moves(point, board);
    if(moves.empty()){
        if(rows_left > 0){
            return PathState::Error;
        }
        if(rows_left <= 0){
            return PathState::Ok;
        }
    }
    PathState state;
    Point_2D next_move = gen_close_path(moves, board);
    board.board_map[board[next_move]] = PointState::Occupied;
    result.push_back(next_move);
    return gen_path(next_move, board, rows_left-1, result);
}

//checa se o ponto é uma notação algébrica de xadrez valida
bool is_valid(std::string point, std::array<std::array<std::string, 8>, 8> &board){
    for(auto x : board){
        for(auto y : x){
            if(point == y){
                return true;
            }
        }
    }
    return false;
}

//retorna as coordenadas do campo de uma notação algébrica de xadrez
Point_2D get_point(std::string point, std::array<std::array<std::string, 8>, 8> &board){
    for(int x = 0; x < 8; x++){
        for(int y = 0; y < 8; y++){
            if(point == board[x][y]){
                return Point_2D(x,y);
            }
        }
    }
    return Point_2D(0,0);
}

int main(int argc, char *argv[]) {
    if(argc < 2){
        std::cout << "Chame esse programa passando uma posição em notação algébrica de xadrez\n";
        std::cout << "exemplo: ./main a1\n";
        return  1;
    }

    std::string start = argv[1];
    auto chess_array = gen_board();
    if(!is_valid(start, chess_array)){
        std::cout << "a posição: " << start << " não é valida!\n";
        return 1;
    }

    auto chess_map = gen_map(start, chess_array);
    auto chess_board = Chess_board(chess_map, chess_array);
    std::vector<Point_2D> result_vector;
    PathState return_state = gen_path(get_point(start, chess_array), chess_board, 63, result_vector);
    switch(return_state){
        case PathState::Ok:
            std::cout << chess_board[get_point(start, chess_array)] << "\n";
            for(auto point : result_vector){
                std::cout << chess_board[point] << "\n";
            }
            break;
        case PathState::Error:
            std::cout << "não foi possivel achar uma solução\n";
            break;
    }
    return 0;
}
