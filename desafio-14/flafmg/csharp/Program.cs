using System.Globalization;

public class Program
{
    private static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("uso correto: dotnet run <caminho_do_arquivo>");
            return;
        }

        var filePath = args[0];
        if (!File.Exists(filePath))
        {
            Console.WriteLine("erro: arquivo especificado não encontrado");
            return;
        }

        var expressions = LoadExpressions(filePath);
        if (expressions == null || expressions.Count == 0)
        {
            Console.WriteLine("erro: arquivo está vazio ou não pode ser lido");
            return;
        }

        foreach (var expression in expressions)
        {
            var result = EvaluateExpression(expression);
            Console.WriteLine(result);
        }
    }

    private static List<string> LoadExpressions(string filePath)
    {
        try
        {
            return File.ReadAllLines(filePath)
                .Select(line => line.Trim())
                .Where(line => !string.IsNullOrWhiteSpace(line))
                .ToList();
        }
        catch
        {
            return null;
        }
    }

    private static string EvaluateExpression(string expression)
    {
        var tokens = Tokenize(expression);
        if (tokens == null)
            return "ERR SYNTAX";

        var rpn = ConvertToRPN(tokens);
        if (rpn == null)
            return "ERR SYNTAX";

        return EvaluateRPN(rpn);
    }

    private static List<string> Tokenize(string expression)
    {
        var tokens = new List<string>();
        var number = "";

        foreach (var ch in expression)
        {
            if (char.IsDigit(ch) || ch == '.')
            {
                number += ch;
                continue;
            }

            if (!string.IsNullOrEmpty(number))
            {
                tokens.Add(number);
                number = "";
            }

            if (!char.IsWhiteSpace(ch))
                tokens.Add(ch.ToString());
        }

        if (!string.IsNullOrEmpty(number))
            tokens.Add(number);

        return tokens;
    }
    // ultiliza notação polonesa inversa https://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_polonesa_inversa
    // para analisar as expressões
    private static List<string> ConvertToRPN(List<string> tokens)
    {
        var output = new List<string>();
        var operators = new Stack<string>();
        var precedence = new Dictionary<string, int>
        {
            { "+", 1 },
            { "-", 1 },
            { "*", 2 },
            { "/", 2 },
            { "^", 3 }
        };

        foreach (var token in tokens)
        {
            if (double.TryParse(token, NumberStyles.Float, CultureInfo.InvariantCulture, out _))
            {
                output.Add(token);
                continue;
            }
            if (token == "(")
            {
                operators.Push(token);
                continue;
            }

            if (token == ")")
            {
                while (operators.Count > 0 && operators.Peek() != "(")
                    output.Add(operators.Pop());

                if (operators.Count == 0 || operators.Pop() != "(")
                    return null;

                continue;
            }

            while (operators.Count > 0 && precedence.ContainsKey(operators.Peek()) && precedence[operators.Peek()] >= precedence[token])
            {
                output.Add(operators.Pop());
            }
            operators.Push(token);
        }

        while (operators.Count > 0)
        {
            var op = operators.Pop();
            if (op == "(" || op == ")") return null;
            output.Add(op);
        }
        return output;
    }

    private static string EvaluateRPN(List<string> rpn)
    {
        var stack = new Stack<double>();

        foreach (var token in rpn)
        {
            if (double.TryParse(token, NumberStyles.Float, CultureInfo.InvariantCulture, out var number))
            {
                stack.Push(number);
                continue;
            }

            if (stack.Count < 2) return "ERR SYNTAX";

            var b = stack.Pop();
            var a = stack.Pop();

            if (token == "/" && b == 0) return "ERR DIVBYZERO";

            stack.Push(token switch
            {
                "+" => a + b,
                "-" => a - b,
                "*" => a * b,
                "/" => a / b,
                "^" => Math.Pow(a, b),
                _ => 0
            });
        }

        return stack.Count == 1 ? stack.Pop().ToString(CultureInfo.InvariantCulture) : "ERR SYNTAX";
    }
}