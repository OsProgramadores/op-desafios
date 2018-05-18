using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Dynamic;
using System.IO;
using System.IO.MemoryMappedFiles;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace desafio5
{
    public class Program
    {
        public Program()
        {
            Process.GetCurrentProcess().PriorityBoostEnabled = true;
        }

        Dictionary<string, KeyValuePair<Type, Delegate>> handlers = new Dictionary<string, KeyValuePair<Type, Delegate>>();
        public void RegisterHandler<T>(string path, Action<T> handler)
        {
            handlers.Add(path, new KeyValuePair<Type, Delegate>(typeof(T), handler));
        }

        public static async void Main(string[] args)
        {
            var program = new Program();
            var filePath = args.Length > 0 ? args[0] : Path.Combine(Environment.CurrentDirectory, "funcionarios.json");

            program.RegisterHandler<Funcionarios>("funcionarios", program.funcionariosHandler);
            program.RegisterHandler<Areas>("areas", program.areasHandler);

            await program.readLinesFromFileAsync(filePath);
        }

        private async Task readLinesFromFileAsync(string filePath)
        {
            if (!File.Exists(filePath))
            {
                WriteLine("O arquivo não existe no destino específicado");
            }
            using (var r = File.OpenText(filePath))
            {
                string line = ""; // Line readed from file

                string propertyName = string.Empty; // Used to retain previous information about property readed
                string propertyReaded = string.Empty;

                var path = new List<string>(); // Track path where manipulating JSON
                Delegate callback = null; // handler for path
                object d = null;
                Type t = null;
                var readLineAsync = r.ReadLineAsync();
                do
                {
                    line = await readLineAsync;
                    readLineAsync = r.ReadLineAsync();

                    for (int i = 0; i < line.Length; i++)
                    {
                        var c = line[i];
                        // Write(c);
                        switch (c)
                        {
                            case '{':
                                {
                                    if (callback != default)
                                    {
                                        d = Activator.CreateInstance(t);
                                    }
                                    continue;
                                }
                            case '}':
                                {
                                    DefineValueToProperty(propertyName, propertyReaded, d, t);
                                    propertyName = propertyReaded = string.Empty;
                                    callback?.DynamicInvoke(d);
                                    continue;
                                }
                            case '[':
                                {
                                    path.Add(propertyName);
                                    var response = GetListener(path);
                                    callback = response.Value;
                                    t = response.Key;
                                    propertyName = propertyReaded = string.Empty;
                                    continue;
                                }
                            case ']':
                                {
                                    callback = null;
                                    path.RemoveAt(path.Count - 1);
                                    propertyName = propertyReaded = string.Empty;
                                    d = null;
                                    t = null;
                                    continue;
                                }
                            case ',':
                                {
                                    DefineValueToProperty(propertyName, propertyReaded, d, t);
                                    propertyName = propertyReaded = string.Empty;
                                    continue;
                                }
                            case '"':
                                {
                                    continue;

                                }
                            case ':':
                                {
                                    propertyName = propertyReaded;
                                    propertyReaded = string.Empty;
                                    continue;
                                }
                            default:
                                {
                                    propertyReaded += c;
                                    continue;
                                }
                        }
                    }
                } while (!r.EndOfStream);
            }
        }

        private void DefineValueToProperty(string propertyName, string propertyReaded, object d, Type t)
        {
            if (!string.IsNullOrEmpty(propertyName))
            {
                var type = t.GetProperty(propertyName).PropertyType;
                var changed = Convert.ChangeType(propertyReaded, type);
                d.GetType().GetProperty(propertyName).SetValue(d, changed);
            }
        }

        private KeyValuePair<Type, Delegate> GetListener(List<string> map)
        {
            string key = string.Join('.', map);

            if (handlers.TryGetValue(key, out var store))
            {
                return store;
            }
            return default;

        }

        private void funcionariosHandler(Funcionarios json)
        {
            WriteLine("json funcionarios " + json);
        }

        private void areasHandler(Areas json)
        {
            WriteLine("json areas" + json);
        }
    }

    public class Funcionarios
    {
        public int id { get; set; }
        public string nome { get; set; }
        public string sobrenome { get; set; }
        public string area { get; set; }
        public float salario { get; set; }

        public override string ToString()
        {
            return $@"{{ 
                id : {id},
                nome : {nome},
                sobrenome : {sobrenome},
                area : {area},
                salario : {salario}
                }}";

        }
    }
    public class Areas
    {
        public string codigo { get; set; }
        public string nome { get; set; }
        public override string ToString()
        {
            return $@"
            {{
                codigo : {codigo},
                nome : {nome}
            }}
            ";
        }
    }

}