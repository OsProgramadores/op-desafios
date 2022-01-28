#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>

#include "json.hpp"

using namespace std;
using json = nlohmann::json;

void Query1(json funcionarios);
void Query2(json funcionarios, json areas);
void Query3(json funcionarios, json areas);
void Query4(json funcionarios);

int main(int argc, char *argv[]) {
    ifstream jsonFileRaw(argv[1]);
    if (!jsonFileRaw.is_open()) {
        cout << "File not found!" << endl;
    } else {
        json data;
        jsonFileRaw >> data;
        json jsonFuncionarios = data["funcionarios"];
        json jsonAreas = data["areas"];
        Query1(jsonFuncionarios);
        Query2(jsonFuncionarios, jsonAreas);
        Query3(jsonFuncionarios, jsonAreas);
        Query4(jsonFuncionarios);
        return 0;
    }
}

void Query1(json funcionarios) {
    unordered_map<float, json> map;
    double salarioTot = 0;
    int count = 0;

    for (const auto funcionario : funcionarios) {
        map[funcionario["salario"]] += funcionario;
        salarioTot += funcionario["salario"].get<float>();
        count++;
    }

    auto [min, max] = minmax_element(
        map.begin(), map.end(),
        [&](auto const &f1, auto const &f2) { return f1.first < f2.first; });

    for (const auto m : max->second) {
        string fullName =
            m["nome"].get<string>() + " " + m["sobrenome"].get<string>();
        cout << "global_max|" << fullName << "|" << setprecision(2) << fixed
             << m["salario"].get<float>() << endl;
    }

    for (const auto m : min->second) {
        string fullName =
            m["nome"].get<string>() + " " + m["sobrenome"].get<string>();
        cout << "global_min|" << fullName << "|" << setprecision(2) << fixed
             << m["salario"].get<float>() << endl;
    }
    cout << setprecision(2) << fixed;
    cout << "global_avg|" << salarioTot / count << endl;
}

void Query2(json funcionarios, json areas) {
    unordered_map<string, json> map;
    unordered_map<string, string> areasMap;
    unordered_map<string, double> salarioTot;
    unordered_map<string, int> countFuncionarios;

    for (const auto area : areas) {
        areasMap[area["codigo"]] = area["nome"];
    }

    for (const auto funcionario : funcionarios) {
        map[funcionario["area"]] += funcionario;
        salarioTot[funcionario["area"]] += funcionario["salario"].get<float>();
        countFuncionarios[funcionario["area"]] += 1;
    }

    unordered_map<float, json> porSalario;
    for (const auto m : map) {
        auto [min, max] =
            minmax_element(m.second.begin(), m.second.end(),
                           [&](auto const &f1, auto const &f2) {
                               return f1["salario"] < f2["salario"];
                           });
        string areaName = areasMap[m.first];
        double averageArea = salarioTot[m.first] / countFuncionarios[m.first];
        for (const auto s : m.second) {
            if (s["salario"] == (*max)["salario"]) {
                string fullName = s["nome"].get<string>() + " " +
                                  s["sobrenome"].get<string>();

                cout << "area_max|" << areaName << "|" << fullName << "|"
                     << setprecision(2) << fixed << s["salario"] << endl;

            } else if (s["salario"] == (*min)["salario"]) {
                string fullName = s["nome"].get<string>() + " " +
                                  s["sobrenome"].get<string>();

                cout << "area_min|" << areaName << "|" << fullName << "|"
                     << setprecision(2) << fixed << s["salario"] << endl;
            }
        }
        cout << "area_avg|" << areaName << "|" << fixed << setprecision(2)
             << averageArea << endl;
    }
}

void Query3(json funcionarios, json areas) {
    unordered_map<string, int> map;
    unordered_map<string, string> areasMap;

    for (const auto area : areas) {
        areasMap[area["codigo"]] = area["nome"];
    }
    for (const auto funcionario : funcionarios) {
        map[funcionario["area"]] += 1;
    }

    auto [min, max] = minmax_element(
        map.begin(), map.end(),
        [&](auto const &f1, auto const &f2) { return f1.second < f2.second; });

    for (auto m : map) {
        string areaName = areasMap[m.first];
        if (m.second == max->second) {
            cout << "most_employees|" << areaName << "|" << m.second << endl;
        } else if (m.second == min->second) {
            cout << "least_employees|" << areaName << "|" << m.second << endl;
        }
    }
}

void Query4(json funcionarios) {
    unordered_map<string, json> map;
    unordered_map<string, int> count;
    unordered_map<string, double> max;

    for (const auto funcionario : funcionarios) {
        map[funcionario["sobrenome"]] += funcionario;
        count[funcionario["sobrenome"]] += 1;
        max[funcionario["sobrenome"]] =
            (funcionario["salario"] > max[funcionario["sobrenome"]])
                ? funcionario["salario"].get<float>()
                : max[funcionario["sobrenome"]];
    }

    for (const auto m : map) {
        int countFuncionarios = count[m.first];
        float salarioAlto = max[m.first];
        if (countFuncionarios > 1) {
            for (auto ma : m.second) {
                if (ma["salario"].get<float>() == salarioAlto) {
                    string fullName = ma["nome"].get<string>() + " " +
                                      ma["sobrenome"].get<string>();
                    cout << "last_name_max|" << ma["sobrenome"].get<string>()
                         << "|" << fullName << "|" << setprecision(2) << fixed
                         << ma["salario"].get<float>() << endl;
                }
            }
        }
    }
}
