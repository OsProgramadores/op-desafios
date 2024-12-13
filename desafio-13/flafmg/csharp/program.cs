using System;
using System.Collections.Generic;
using System.Diagnostics;

class Program
{
    private const int BoardSize = 8;
    public record Position(int X, int Y);
    static readonly Position[] HorseMoves = new Position[]
    {
        new Position(2, 1), new Position(1, 2), new Position(-1, 2), new Position(-2, 1),
        new Position(-2, -1), new Position(-1, -2), new Position(1, -2), new Position(2, -1)
    };
    static void Main(string[] args)
    {
        if (args.Length != 1)
        {
            Console.WriteLine("uso correto: dotnet run <posição inicial>");
            return;
        }

        string startPosition = args[0];
        Position start = AlgebraicToPosition(startPosition);
        var visited = new HashSet<Position> { start };
        var path = new List<Position> { start };
        var stopwatch = Stopwatch.StartNew();

        if (Warnsdorff(start, visited, path))
        {
            Console.WriteLine("solução encontrada:");
            foreach (var pos in path)
            {
                Console.WriteLine(PositionToAlgebraic(pos));
            }
        }
        else
        {
            Console.WriteLine("nenhuma solução encontrada.");
        }

        stopwatch.Stop();

        #if DEBUG
        Console.WriteLine($"tempo de execução: {stopwatch.ElapsedMilliseconds} ms");
        #endif
    }

    static bool Warnsdorff(Position currentPosition, HashSet<Position> visited, List<Position> path)
    {
        if (visited.Count == BoardSize * BoardSize)
        {
            return true;
        }
        var moves = new List<(Position Next, int Degree)>();
        foreach (var move in HorseMoves)
        {
            Position next = new Position(currentPosition.X + move.X, currentPosition.Y + move.Y);
            if (IsInBounds(next) && !visited.Contains(next))
            {
                int degree = CountAvailableMoves(next, visited);
                moves.Add((next, degree));
            }
        }
        moves.Sort((a, b) => a.Degree.CompareTo(b.Degree));
        foreach (var move in moves)
        {
            visited.Add(move.Next);
            path.Add(move.Next);
            if (Warnsdorff(move.Next, visited, path))
            {
                return true;
            }
            
            visited.Remove(move.Next);
            path.RemoveAt(path.Count - 1);
        }

        return false;
    }

    static int CountAvailableMoves(Position position, HashSet<Position> visited)
    {
        int count = 0;
        foreach (var move in HorseMoves)
        {
            Position next = new Position(position.X + move.X, position.Y + move.Y);
            if (IsInBounds(next) && !visited.Contains(next))
            {
                count++ ;
            }
        }
        return count;
    }

    static bool IsInBounds(Position position)
    {
        return position.X >= 0 && position.X < BoardSize && position.Y >= 0 && position.Y < BoardSize;
    }

    public static string PositionToAlgebraic(Position position)
    {
        return $"{(char)('a' + position.X)}{(char)('1' + position.Y)}";
    }
    static Position AlgebraicToPosition(string position)
    {
        return new Position(position[0] - 'a', position[1] - '1');
    }
}
