#include <fstream>
#include <iostream>

using namespace std;

void reverse(string& str) {
    int n = str.length();
    for (int i = 0; i < n / 2; i++) {
        swap(str[i], str[n - i - 1]);
    }
}

int main(int argc, char* argv[]) {
    ifstream file(argv[1]);
    if (!file.is_open()) {
        cout << "File not found." << endl;
        return 1;
    }
    char initialChar = file.get();
    char c;
    string buffer;
    int pos;
    file.seekg(-1, ios::end);
    pos = file.tellg();
    for (int i = 0; i < pos + 1; i++) {
        c = file.get();
        if (c == '\n' || file.tellg() == 1) {
            if (file.tellg() == 1) {
                buffer += c;
            }
            reverse(buffer);
            cout << buffer;
            buffer = "";
        }
        buffer += c;
        file.seekg(-2, ios::cur);
    }
    if (initialChar == '\n') {
        cout << endl;
    }
    return 0;
}
