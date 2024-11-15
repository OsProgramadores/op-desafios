// .--------------------------.
// | desafio 10 por @flafmg.  |
// `--------------------------´
class Program
{
    private static bool debug = false;

    static void Main(string[] args)
    {
        if (args.Length < 1)
        {
            Console.WriteLine("Forneça o arquivo de dados como argumento.");
            return;
        }

        var dataFilePath = args[0];
        if (!File.Exists(dataFilePath))
        {
            Console.WriteLine($"Arquivo de dados não encontrado: {dataFilePath}");
            return;
        }

        var dataLines = File.ReadAllLines(dataFilePath);
        var results = new List<string>();

        foreach (var line in dataLines)
        {
            if (string.IsNullOrWhiteSpace(line)) continue;

            var parts = line.Split(',');
            if (parts.Length != 2)
            {
                Console.WriteLine($"Linha inválida no arquivo de dados: {line}");
                continue;
            }

            var ruleFilePath = Path.Combine(Path.GetDirectoryName(dataFilePath) ?? string.Empty, parts[0].Trim());
            var ruleFileName = Path.GetFileName(parts[0].Trim());
            var input = parts[1].Trim();

            if (!File.Exists(ruleFilePath))
            {
                Console.WriteLine($"arquivo de regras não encontrado: {ruleFilePath}");
                continue;
            }

            var rules = ReadRules(ruleFilePath);
            if (rules == null)
            {
                Console.WriteLine($"erro ao ler o arquivo de regras: {ruleFilePath}");
                continue;
            }

            var output = ExecuteTuringMachine(rules, input, ruleFileName);
            results.Add($"{ruleFileName},{input},{output}");
        }

        foreach (var result in results)
        {
            Console.WriteLine(result);
        }
    }

    static List<Rule> ReadRules(string ruleFilePath)
    {
        try
        {
            var lines = File.ReadAllLines(ruleFilePath);
            var rules = new List<Rule>();

            foreach (var line in lines)
            {
                var trimmedLine = line.Split(';')[0].Trim();
                if (string.IsNullOrWhiteSpace(trimmedLine)) continue;

                var parts = trimmedLine.Split(' ', StringSplitOptions.RemoveEmptyEntries);
                if (parts.Length != 5)
                {
                    throw new FormatException("regra com formato invalido");
                }

                rules.Add(new Rule(parts[0], parts[1], parts[2], parts[3], parts[4]));
            }

            return rules;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"erro ao ler regras: {ex.Message}");
            return null;
        }
    }

    static string ExecuteTuringMachine(List<Rule> rules, string tape, string ruleFileName)
    {
        var tapeList = new List<char>(tape.ToCharArray());
        var head = 0;
        var state = "0";

        while (true)
        {
            if (head < 0)
            {
                tapeList.Insert(0, ' ');
                head = 0;
            }
            else if (head >= tapeList.Count)
            {
                tapeList.Add(' ');
            }

            var currentSymbol = tapeList[head];
            var applicableRule = GetApplicableRule(rules, state, currentSymbol);

            if (applicableRule == null)
            {
                return "ERR";
            }

            if (debug)
            {
                Console.WriteLine(
                    $"Arquivo: {ruleFileName}, Estado: {state}, Símbolo: {currentSymbol}, Regra: {applicableRule}");
            }

            if (applicableRule.NewSymbol != "*")
            {
                tapeList[head] = applicableRule.NewSymbol == "_" ? ' ' : applicableRule.NewSymbol[0];
            }

            head += applicableRule.Direction switch //simplificação dos ifs
            {
                "l" => -1,
                "r" => 1,
                "*" => 0,
                _ => throw new InvalidOperationException("direção de movimento inesistente")
            };

            state = applicableRule.NewState;

            if (state.StartsWith("halt"))
            {
                break;
            }
        }

        return new string(tapeList.ToArray()).Trim();
    }

    static Rule GetApplicableRule(List<Rule> rules, string currentState, char currentSymbol) //simplificação das rules
    {
        return rules.FirstOrDefault(r =>
                   r.CurrentState == currentState &&
                   (r.CurrentSymbol == currentSymbol.ToString() || (r.CurrentSymbol == "_" && currentSymbol == ' ')))
               ?? rules.FirstOrDefault(r =>
                   r.CurrentState == "*" &&
                   (r.CurrentSymbol == currentSymbol.ToString() || (r.CurrentSymbol == "_" && currentSymbol == ' ')))
               ?? rules.FirstOrDefault(r =>
                   r.CurrentState == currentState &&
                   r.CurrentSymbol == "*")
               ?? rules.FirstOrDefault(r =>
                   r.CurrentState == "*" &&
                   r.CurrentSymbol == "*");
    }
}
class Rule
{
    public string CurrentState { get; }
    public string CurrentSymbol { get; }
    public string NewSymbol { get; }
    public string Direction { get; }
    public string NewState { get; }

    public Rule(string currentState, string currentSymbol, string newSymbol, string direction, string newState)
    {
        CurrentState = currentState;
        CurrentSymbol = currentSymbol;
        NewSymbol = newSymbol;
        Direction = direction;
        NewState = newState;
    }

    public override string ToString()
    {
        return $"{CurrentState} {CurrentSymbol} {NewSymbol} {Direction} {NewState}";
    }
}
