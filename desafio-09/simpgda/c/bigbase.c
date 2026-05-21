#include <stdio.h>
#include <string.h>
#include <stdbool.h>

const char CHARSET[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

// Retorna o valor numérico de um caractere, ou -1 se for inválido
int char_to_val(char c) {
    if (c >= '0' && c <= '9') return c - '0';
    if (c >= 'A' && c <= 'Z') return c - 'A' + 10;
    if (c >= 'a' && c <= 'z') return c - 'a' + 36;
    return -1;
}

// Analisa a string de entrada, ignora zeros à esquerda e popula o vetor de dígitos
bool parse_number(const char* str, int base_in, int* digits, int* len) {
    *len = 0;
    int start = 0;
    
    // Rejeita número negativo de cara
    if (str[0] == '-') return false;
    
    // Pula zeros à esquerda para o tamanho do vetor refletir a grandeza real do número
    while (str[start] == '0' && str[start+1] != '\0') {
        start++;
    }

    for (int i = start; str[i] != '\0'; i++) {
        int val = char_to_val(str[i]);
        if (val < 0 || val >= base_in) return false;
        digits[(*len)++] = val;
    }
    
    // Se a entrada for apenas "000", garante que o array não fique vazio
    if (*len == 0 && str[start] == '0') {
        digits[0] = 0;
        *len = 1;
    }
    
    return true;
}

// Algoritmo de divisão sucessiva para converter bases arbitrariamente grandes
void convert_base(const int* in_digits, int in_len, int base_in, int base_out, char* out_str) {
    int digits[2048];
    for (int i = 0; i < in_len; i++) digits[i] = in_digits[i];
    int len = in_len;

    char result[2048];
    int res_len = 0;

    // Caso especial para o número zero
    if (len == 1 && digits[0] == 0) {
        out_str[0] = '0';
        out_str[1] = '\0';
        return;
    }

    // Faz a divisão contínua do vetor inteiro
    while (len > 0) {
        unsigned long long remainder = 0;
        int next_len = 0;
        int next_digits[2048];

        for (int i = 0; i < len; i++) {
            remainder = remainder * base_in + digits[i];
            int div = remainder / base_out;
            remainder = remainder % base_out;

            // Só adiciona ao próximo vetor quando o quociente deixa de ser zero
            if (next_len > 0 || div > 0) {
                next_digits[next_len++] = div;
            }
        }
        
        result[res_len++] = CHARSET[remainder];

        // Atualiza os dígitos para a próxima rodada de divisão
        for (int i = 0; i < next_len; i++) digits[i] = next_digits[i];
        len = next_len;
    }

    // Inverte o resultado para gerar a string final correta
    for (int i = 0; i < res_len; i++) {
        out_str[i] = result[res_len - 1 - i];
    }
    out_str[res_len] = '\0';
}

int main(void) {
    char linha[4096];
    
    while (fgets(linha, sizeof(linha), stdin)) {
        linha[strcspn(linha, "\r\n")] = '\0';
        if (strlen(linha) == 0) continue;

        int base_in = 0, base_out = 0;
        char num_str[2048];
        
        if (sscanf(linha, "%d %d %2047s", &base_in, &base_out, num_str) == 3) {
            
            if (base_in < 2 || base_in > 62 || base_out < 2 || base_out > 62) {
                printf("???\n");
                continue;
            }
            
            int digits[2048];
            int len = 0;
            
            // Tenta analisar; se tiver caractere inválido, cospe erro
            if (!parse_number(num_str, base_in, digits, &len)) {
                printf("???\n");
                continue;
            }
            
            // Converte silenciosamente para base 62 só para medir o limite do desafio
            char out_62[2048];
            convert_base(digits, len, base_in, 62, out_62);
            
            // O desafio estipula o tamanho máximo como 30 caracteres na base 62
            if (strlen(out_62) > 30) {
                printf("???\n");
                continue;
            }
            
            // Passou em todos os limites. Faz a conversão final solicitada.
            char out_final[2048];
            convert_base(digits, len, base_in, base_out, out_final);
            
            printf("%s\n", out_final);
        }
    }
    return 0;
}