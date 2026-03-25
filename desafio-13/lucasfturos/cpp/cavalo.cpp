#include <algorithm>
#include <chrono>
#include <iostream>
#include <regex>
#include <string>
#include <thread>
#include <vector>

struct Position {
    int x;
    int y;
    int move_count;
};

const int board_size = 8;
const std::string color_clear = "\e[0m";
const std::string color_red = "\e[41;1m";
const std::string color_black = "\e[40m";
const std::string color_white = "\e[107m";
const std::string color_bw = "\e[30;107;1m";
const int move_x[] = {-2, -1, 1, 2, 2, 1, -1, -2};
const int move_y[] = {1, 2, 2, 1, -1, -2, -2, -1};
std::vector<std::vector<std::string>>
    print_board(board_size, std::vector<std::string>(board_size));
std::vector<std::vector<int>> move_count_board(board_size,
                                               std::vector<int>(board_size, 0));

int validaEntrada(std::string input) {
    std::regex pattern("^[a-h][1-8]$");

    if (std::regex_match(input, pattern)) {
        return true;
    }

    return false;
}

int isValidMove(int x, int y,
                const std::vector<std::vector<int>> &passou_cavalo) {
    return (x >= 0 && x < board_size && y >= 0 && y < board_size &&
            !passou_cavalo[x][y]);
}

int countCasasVizinhas(int x, int y,
                       const std::vector<std::vector<int>> &passou_cavalo) {

    int count = 0;

    for (int i = 0; i < 8; i++) {
        int nextX = x + move_x[i];
        int nextY = y + move_y[i];

        if (isValidMove(nextX, nextY, passou_cavalo)) {
            count++;
        }
    }

    return count;
}

bool comparaCasasVizinhas(const Position &pos1, const Position &pos2,
                          const std::vector<std::vector<int>> &passou_cavalo) {
    return countCasasVizinhas(pos1.x, pos1.y, passou_cavalo) <
           countCasasVizinhas(pos2.x, pos2.y, passou_cavalo);
}

bool resolvePasseioCavalo(int x, int y, int move_count,
                          std::vector<std::vector<int>> &passou_cavalo,
                          std::vector<Position> &rota_cavalo) {
    passou_cavalo[x][y] = true;
    rota_cavalo.push_back({x, y, move_count});

    if (move_count == board_size * board_size) {
        return true;
    }

    std::vector<Position> casas_vizinhas;

    for (int i = 0; i < 8; i++) {
        int nextX = x + move_x[i];
        int nextY = y + move_y[i];

        if (isValidMove(nextX, nextY, passou_cavalo)) {
            casas_vizinhas.push_back({nextX, nextY, move_count});
        }
    }

    std::sort(casas_vizinhas.begin(), casas_vizinhas.end(),
              [&](const Position &pos1, const Position &pos2) {
                  return comparaCasasVizinhas(pos1, pos2, passou_cavalo);
              });

    for (const auto &casa_vizinha : casas_vizinhas) {
        if (resolvePasseioCavalo(casa_vizinha.x, casa_vizinha.y, move_count + 1,
                                 passou_cavalo, rota_cavalo)) {
            return true;
        }
    }

    rota_cavalo.pop_back();
    passou_cavalo[x][y] = false;

    return false;
}

void printPasseioCavalo(const std::vector<Position> &rota_cavalo) {
    std::cout << "Log das posições percorridas:" << '\n';
    for (const auto &pos : rota_cavalo) {
        char c = 'a' + pos.y;
        char num = '1' + pos.x;
        std::cout << c << num << '\n';
    }
}

void drawTabuleiro(const Position &pos) {
    for (int row = 0; row < board_size; row++) {
        std::string str_row;
        int indice = 8 - row;
        str_row += color_clear + " " + std::to_string(indice) + ' ';
        for (int col = 0; col < board_size; col++) {
            if (board_size - 1 - row == pos.x && col == pos.y) {
                if (pos.move_count <= 9) {
                    str_row += color_red + " " + std::to_string(pos.move_count);
                } else {
                    str_row += color_red + std::to_string(pos.move_count);
                }
                move_count_board[row][col] = pos.move_count;
            } else if ((row + col) % 2) {
                if (move_count_board[row][col] != 0) {
                    if (move_count_board[row][col] <= 9) {
                        str_row += color_bw + " " +
                                   std::to_string(move_count_board[row][col]);
                    } else {
                        str_row += color_bw +
                                   std::to_string(move_count_board[row][col]);
                    }
                } else {
                    str_row += color_white + "  ";
                }
            } else {
                if (move_count_board[row][col] != 0) {
                    if (move_count_board[row][col] <= 9) {
                        str_row += color_clear + " " +
                                   std::to_string(move_count_board[row][col]);
                    } else {
                        str_row += color_clear +
                                   std::to_string(move_count_board[row][col]);
                    }
                } else {
                    str_row += color_black + "  ";
                }
            }
        }

        str_row += color_clear + " " + std::to_string(indice) + '\n';
        print_board[row][0] = str_row;
    }
}

void printTabuleiro(const Position &pos) {
    drawTabuleiro(pos);
    std::cout << "\033c";
    std::cout << "   a b c d e f g h" << '\n';
    for (int row = 0; row < board_size; row++) {
        for (int col = 0; col < board_size; col++) {
            std::cout << print_board[row][col];
        }
    }
    std::cout << "   a b c d e f g h" << '\n';
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cerr << "Informe uma entrada para o cavalo passear!!!" << '\n';
        std::exit(1);
    }

    std::string input_pos{argv[1]};
    std::transform(input_pos.begin(), input_pos.end(), input_pos.begin(),
                   ::tolower);
    std::cout << input_pos << '\n';

    if (!validaEntrada(input_pos)) {
        std::cerr << "Entrada inválida!" << '\n' << '\n';
        std::exit(1);
    }

    int startX = input_pos[1] - '1';
    int startY = input_pos[0] - 'a';

    std::vector<Position> rota_cavalo;
    std::vector<std::vector<int>> passou_cavalo(
        board_size, std::vector<int>(board_size, false));

    if (resolvePasseioCavalo(startX, startY, 1, passou_cavalo, rota_cavalo)) {
        for (const auto &pos : rota_cavalo) {
            printTabuleiro(pos);
            std::this_thread::sleep_for(std::chrono::milliseconds(50));
        }
        printPasseioCavalo(rota_cavalo);
    } else {
        std::cerr << "Não foi possível encontrar um caminho válido!" << '\n';
    }

    return 0;
}
