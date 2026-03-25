using System;
using System.IO;
using System.Globalization;
using System.Collections.Generic;

namespace ExpressoesNumericas
{
    class Program
    {
        static double AvaliaExpressao(string expressao)
        {
            if (string.IsNullOrEmpty(expressao))
            {
                throw new Exception("ERR SYNTAX");
            }

            expressao = expressao.Replace(" ", "");

            var numeros = new Stack<double>();
            var operadores = new Stack<char>();

            for (int i = 0; i < expressao.Length; i++)
            {
                char caractere = expressao[i];

                if (char.IsDigit(caractere) || caractere == '.')
                {
                    string numeroString = "";
                    while (
                        i < expressao.Length && (char.IsDigit(expressao[i]) || expressao[i] == '.')
                    )
                    {
                        numeroString += expressao[i];
                        i++;
                    }
                    i--;

                    double numero;
                    if (
                        !double.TryParse(
                            numeroString,
                            NumberStyles.Any,
                            CultureInfo.InvariantCulture,
                            out numero
                        )
                    )
                    {
                        throw new Exception("ERR SYNTAX");
                    }
                    numeros.Push(numero);
                }
                else
                    switch (caractere)
                    {
                        case '(':
                            operadores.Push(caractere);
                            break;
                        case ')':
                        {
                            while (operadores.Count > 0 && operadores.Peek() != '(')
                            {
                                RealizaOperacao(numeros, operadores);
                            }

                            if (operadores.Count == 0 || operadores.Peek() != '(')
                            {
                                throw new Exception("ERR SYNTAX");
                            }

                            operadores.Pop();
                            break;
                        }
                        default:
                        {
                            if (IsOperador(caractere))
                            {
                                while (
                                    operadores.Count > 0
                                    && operadores.Peek() != '('
                                    && ObtemPrecedencia(caractere)
                                        <= ObtemPrecedencia(operadores.Peek())
                                )
                                {
                                    RealizaOperacao(numeros, operadores);
                                }

                                operadores.Push(caractere);
                            }
                            else
                            {
                                throw new Exception("ERR SYNTAX");
                            }
                            break;
                        }
                    }
            }

            while (operadores.Count > 0)
            {
                if (operadores.Peek() == '(' || operadores.Peek() == ')')
                {
                    throw new Exception("ERR SYNTAX");
                }
                RealizaOperacao(numeros, operadores);
            }

            if (numeros.Count != 1)
            {
                throw new Exception("ERR SYNTAX");
            }

            return numeros.Pop();
        }

        static void RealizaOperacao(Stack<double> numeros, Stack<char> operadores)
        {
            if (numeros.Count < 2 || operadores.Count < 1)
            {
                throw new Exception("ERR SYNTAX");
            }

            var num2 = numeros.Pop();
            var num1 = numeros.Pop();
            var operador = operadores.Pop();
            var resultado = AplicaOperacao(num1, num2, operador);
            numeros.Push(resultado);
        }

        static double AplicaOperacao(double num1, double num2, char operador)
        {
            switch (operador)
            {
                case '+':
                    return num1 + num2;
                case '-':
                    return num1 - num2;
                case '*':
                    return num1 * num2;
                case '/':
                    if (num2 == 0)
                    {
                        throw new DivideByZeroException("ERR DIVBYZERO");
                    }
                    return num1 / num2;
                case '^':
                    return Math.Pow(num1, num2);
                default:
                    throw new Exception("ERR SYNTAX");
            }
        }

        static bool IsOperador(char caractere)
        {
            return caractere == '+'
                || caractere == '-'
                || caractere == '*'
                || caractere == '/'
                || caractere == '^';
        }

        static int ObtemPrecedencia(char operador)
        {
            switch (operador)
            {
                case '+':
                case '-':
                    return 1;
                case '*':
                case '/':
                    return 2;
                case '^':
                    return 3;
                default:
                    return 0;
            }
        }

        static void Main(string[] args)
        {
            try
            {
                var expressoes = File.ReadAllLines(args[0]);

                foreach (var expressao in expressoes)
                {
                    try
                    {
                        var resultado = AvaliaExpressao(expressao);
                        Console.WriteLine(resultado.ToString("0.#", CultureInfo.InvariantCulture));
                    }
                    catch (DivideByZeroException)
                    {
                        Console.WriteLine("ERR DIVBYZERO");
                    }
                    catch (Exception)
                    {
                        Console.WriteLine("ERR SYNTAX");
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Exception: " + e.Message);
            }
        }
    }
}
