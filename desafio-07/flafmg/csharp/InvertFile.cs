using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

class Program
{
    const int BlockSize = 100;
    const int BufferSize = BlockSize * 1024 * 1024;

    static void Main(string[] args)
    {
        if (args.Length != 1)
        {
            Console.WriteLine("argumentos vazios, passe o local do arquivo nos argumentos");
            return;
        }

        string filePath = args[0];
        long fileLength, position;
        byte[] buffer;
        var leftoverLine = new LinkedList<byte>();

        try
        {
            using (var fs = new FileStream(filePath, FileMode.Open, FileAccess.Read))
            {
                fileLength = fs.Length;

                do
                {
                    position = (fileLength - BufferSize) < 0 ? 0 : (fileLength - BufferSize);
                    fs.Seek(position, SeekOrigin.Begin);

                    buffer = new byte[fileLength - position];
                    fs.Read(buffer, 0, buffer.Length);

                    ProcessBuffer(buffer, leftoverLine);

                    fileLength = position;

                } while (fileLength > 0);

                PrintString(leftoverLine);
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"erro: {e.Message}");
        }
    }

    static void ProcessBuffer(byte[] buffer, LinkedList<byte> leftoverLine)
    {
        for (int i = buffer.Length - 1; i >= 0; i--)
        {
            if (buffer[i] == '\n')
            {
                PrintString(leftoverLine);
            }

            leftoverLine.AddFirst(buffer[i]);
        }
    }

    static void PrintString(LinkedList<byte> leftoverLine)
    {
        if (leftoverLine.Count > 0)
        {
            byte[] bytes = new byte[leftoverLine.Count];
            int index = 0;

            while (leftoverLine.Count > 0)
            {
                if (leftoverLine.First != null)
                {
                    bytes[index++] = leftoverLine.First.Value;
                    leftoverLine.RemoveFirst();
                }
            }

            string output = Encoding.UTF8.GetString(bytes);
            Console.Write(output);
        }
    }
}
