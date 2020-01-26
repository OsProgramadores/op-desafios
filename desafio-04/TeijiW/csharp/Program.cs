using System;
using System.Collections.Generic;

class MainClass
{

    public static Dictionary<int, int> countParts(List<int> originalList)
    {
        int count = 0;
        Dictionary<int, int> parts = new Dictionary<int, int>();

        for (int i = 0; i <= 6; i++)
        {
            count = 0;
            foreach (int j in originalList.FindAll(x => x == i))
            {
                count++;
            }
            parts[i] = count;

        }
        // Peão 1
        // Bispo 2
        // Cavalo 3
        // Torre 4
        // Rainha 5
        // Rei 6
        return parts;
    }

    public static void Main(string[] args)
    {
        string[] partsName = new string[7] { "", "Peão", "Bispo", "Cavalo", "Torre", "Rainha", "Rei" };
        int[,] table = new int[8, 8] { { 1, 2, 3, 4, 5, 6, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 0 },
        }; // Cada conjunto de chave é uma linha (row) e cada elemento dentro do conjunto é uma coluna (column)

        List<int> listOfParts = new List<int>();

        for (int i = 0; i < table.GetLength(0); i++)
        {
            for (int j = 0; j < table.GetLength(1); j++)
            {
                listOfParts.Add(table[i, j]);
            }
        }

        Dictionary<int, int> parts = countParts(listOfParts);
        for (int i = 1; i <= 6; i++)
        {
            Console.WriteLine($"{partsName[i]} = {parts[i]}");
        }

    }
}