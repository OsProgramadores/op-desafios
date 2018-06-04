using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Dynamic;
using System.Globalization;
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
        public static async Task Main(string[] args)
        {
            var program = new Program();
            var filePath = args.Length > 0 ? args[0] : Path.Combine(Environment.CurrentDirectory, "funcionarios.json");

            program.RegisterHandler<Funcionario>("funcionarios", program.funcionariosHandler);
            program.RegisterHandler<Areas>("areas", program.areasHandler);

            await program.readLinesFromFileAndInvokeHandlersAsync(filePath);


            #region Print reports


            #region 1.
            foreach (var item in program.thoseWhoIncomeLess.employees)
            {
                WriteLine("global_min|{0}|{1:f2}", item.FullName, program.thoseWhoIncomeLess.minSalary);
            }

            foreach (var item in program.thoseWhoIncomeMore.employees)
            {
                WriteLine("global_max|{0}|{1:f2}", item.FullName, program.thoseWhoIncomeMore.maxSalary);
            }

            WriteLine("global_avg|{0:f2}", (program.averageSalary.total / program.averageSalary.employess));
            #endregion


            #region 2.
            foreach (var item in program.salaryPerArea)
            {
                string areaName = program.areas[item.Key];

                var (minSalaryOfArea, maxSalaryOfArea, thoseWhoIncomeLessOfArea, thoseWhoIncomeMoreOfArea) = item.Value;

                foreach (var employe in thoseWhoIncomeLessOfArea)
                {
                    WriteLine("area_min|{0}|{1}|{2:f2}", areaName, employe.FullName, minSalaryOfArea);
                }
                foreach (var employe in thoseWhoIncomeMoreOfArea)
                {
                    WriteLine("area_max|{0}|{1}|{2:f2}", areaName, employe.FullName, maxSalaryOfArea);
                }

                var countPerArea = program.averageSalaryPerArea[item.Key];
                float averagePerArea = countPerArea.totalSalaryOfArea / countPerArea.employesOfArea;
                WriteLine("area_avg|{0}|{1:f2}", areaName, averagePerArea);
            }
            #endregion


            #region 3.
            var (minEmployees, maxEmployes) = (int.MaxValue, 0);
            var (minArea, maxArea) = ("", "");
            foreach (var area in program.averageSalaryPerArea)
            {
                int employesOfArea = area.Value.employesOfArea;
                if (employesOfArea < minEmployees)
                {
                    minArea = area.Key;
                    minEmployees = employesOfArea;
                }
                if (employesOfArea > maxEmployes)
                {
                    maxArea = area.Key;
                    maxEmployes = employesOfArea;
                }

            }
            WriteLine("least_employees|{0}|{1}", program.areas[minArea], minEmployees);
            WriteLine("most_employees|{0}|{1}", program.areas[maxArea], maxEmployes);
            #endregion


            #region 4.
            foreach (var employeWithSameLastNameWhoIncomesMore in program.employeesWithSameLastNameWhoIncomesMore)
            {
                var value = employeWithSameLastNameWhoIncomesMore.Value;
                foreach (var employe in value.employees)
                {
                    if (value.numberOfEmployees > 1)
                    {
                        WriteLine("last_name_max|{0}|{1}|{2:f2}", employeWithSameLastNameWhoIncomesMore.Key, employe.FullName, value.salary);
                    }
                }
            }
            #endregion


            #endregion
        }

        Dictionary<string, (Type T, Delegate callback)> handlers = new Dictionary<string, (Type, Delegate)>();
        public void RegisterHandler<T>(string path, Action<T> handler)
        {
            handlers.Add(path, (typeof(T), handler));
        }

        private async Task readLinesFromFileAndInvokeHandlersAsync(string filePath)
        {
            if (!File.Exists(filePath))
            {
                WriteLine("O arquivo não existe no destino específicado");
            }
            using (var r = File.OpenText(filePath))
            {
                // var readLineAsync = r.ReadLineAsync(); // Task to reduce idle time reading file
                string line = ""; // Line readed from file

                string propertyName = string.Empty; // Used to retain previous information about property readed
                string propertyReaded = string.Empty; // Used as temporary value

                var path = new List<string>(); // Track path where we're manipulating JSON to allow callback's call
                Delegate callback = null; // callback for path
                object objectBeingParsed = null; // Dinamic object used to persist strongly typed information about JSON parsed
                Type typeOfObjectBeingParsed = null; // Strong type to callback's 

                do
                {
                    line = await r.ReadLineAsync();


                    for (int i = 0; i < line.Length; i++)
                    {
                        var c = line[i];
                        switch (c)
                        {
                            case '{':
                                {
                                    if (callback != null)
                                    {
                                        objectBeingParsed = Activator.CreateInstance(typeOfObjectBeingParsed);
                                    }
                                    continue;
                                }
                            case '}':
                                {
                                    DefineValueToProperty(ref propertyName, ref propertyReaded, objectBeingParsed, typeOfObjectBeingParsed);
                                    callback?.DynamicInvoke(objectBeingParsed);
                                    continue;
                                }
                            case '[':
                                {
                                    path.Add(propertyName.Trim());
                                    var response = GetListener(path);
                                    (typeOfObjectBeingParsed, callback) = response;
                                    propertyName = propertyReaded = string.Empty;
                                    continue;
                                }
                            case ']':
                                {
                                    callback = null;
                                    path.RemoveAt(path.Count - 1);
                                    propertyName = propertyReaded = string.Empty;
                                    objectBeingParsed = null;
                                    typeOfObjectBeingParsed = null;
                                    continue;
                                }
                            case ',':
                                {
                                    DefineValueToProperty(ref propertyName, ref propertyReaded, objectBeingParsed, typeOfObjectBeingParsed);
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

            #region Support Functions
            (Type, Delegate) GetListener(List<string> map)
            {
                string key = string.Join('.', map);

                if (handlers.TryGetValue(key, out var store))
                {
                    return (store.T, store.callback);
                }
                return default;
            }

            void DefineValueToProperty(ref string propertyName, ref string propertyReaded, object d, Type t)
            {
                if (!string.IsNullOrEmpty(propertyName))
                {
                    propertyName = propertyName.Trim();
                    propertyReaded = propertyReaded.Trim();
                    var type = t.GetProperty(propertyName).PropertyType;
                    var changed = (type == propertyReaded.GetType())
                        ? propertyReaded
                        : Convert.ChangeType(propertyReaded, type, new CultureInfo("en-US"));
                    t.GetProperty(propertyName).SetValue(d, changed);
                    propertyName = propertyReaded = string.Empty;
                }
            }
            #endregion
        }


        (float minSalary, List<Funcionario> employees) thoseWhoIncomeLess = (float.MaxValue, new List<Funcionario>());
        (float maxSalary, List<Funcionario> employees) thoseWhoIncomeMore = (0, new List<Funcionario>());
        (int employess, double total) averageSalary = (0, 0);
        Dictionary<string, (int employesOfArea, float totalSalaryOfArea)> averageSalaryPerArea = new Dictionary<string, (int, float)>();
        Dictionary<string, (float minSalary, float maxSalary, List<Funcionario> incomeLess, List<Funcionario> incomeMore)> salaryPerArea = new Dictionary<string, (float minSalary, float maxSalary, List<Funcionario> incomeLess, List<Funcionario> incomeMore)>();
        Dictionary<string, (int numberOfEmployees, float salary, List<Funcionario> employees)> employeesWithSameLastNameWhoIncomesMore = new Dictionary<string, (int, float, List<Funcionario>)>();
        Dictionary<string, string> areas = new Dictionary<string, string>();
        private void funcionariosHandler(Funcionario employe)
        {
            #region 1.
            averageSalary.employess++;
            averageSalary.total += employe.salario;

            if (employe.salario < thoseWhoIncomeLess.minSalary)
            {
                thoseWhoIncomeLess.minSalary = employe.salario;
                thoseWhoIncomeLess.employees.Clear();
                thoseWhoIncomeLess.employees.Add(employe);
            }
            else
            if (employe.salario == thoseWhoIncomeLess.minSalary)
            {
                thoseWhoIncomeLess.employees.Add(employe);
            }
            if (employe.salario == thoseWhoIncomeMore.maxSalary)
            {
                thoseWhoIncomeMore.employees.Add(employe);
            }
            else
            if (employe.salario > thoseWhoIncomeMore.maxSalary)
            {
                thoseWhoIncomeMore.maxSalary = employe.salario;
                thoseWhoIncomeMore.employees.Clear();
                thoseWhoIncomeMore.employees.Add(employe);
            }
            #endregion


            #region 2.
            if (!averageSalaryPerArea.TryGetValue(employe.area, out var salaryPerArea))
            {
                averageSalaryPerArea.Add(
                    employe.area,
                    salaryPerArea = (0, 0)
                );
            }
            salaryPerArea.employesOfArea++;
            salaryPerArea.totalSalaryOfArea += employe.salario;
            averageSalaryPerArea[employe.area] = salaryPerArea;

            if (!this.salaryPerArea.TryGetValue(employe.area, out var listPerArea))
            {
                this.salaryPerArea.Add(
                    employe.area,
                    listPerArea = (float.MaxValue, 0, new List<Funcionario>(), new List<Funcionario>())
                );
            }

            if (employe.salario < listPerArea.minSalary)
            {
                listPerArea.minSalary = employe.salario;
                listPerArea.incomeLess.Clear();
                listPerArea.incomeLess.Add(employe);
            }
            else // ^OR
            if (employe.salario == listPerArea.minSalary)
            {
                listPerArea.incomeLess.Add(employe);
            }
            if (employe.salario == listPerArea.maxSalary)
            {
                listPerArea.incomeMore.Add(employe);
            }
            else // ^OR
            if (employe.salario > listPerArea.maxSalary)
            {
                listPerArea.maxSalary = employe.salario;
                listPerArea.incomeMore.Clear();
                listPerArea.incomeMore.Add(employe);
            }
            #endregion
            this.salaryPerArea[employe.area] = listPerArea;



            #region 4.
            if (!employeesWithSameLastNameWhoIncomesMore.TryGetValue(employe.sobrenome, out var employeWithSameLastNameWhoIncomesMore))
            {
                employeesWithSameLastNameWhoIncomesMore.Add(
                    employe.sobrenome,
                    employeWithSameLastNameWhoIncomesMore = (0, 0, new List<Funcionario>())
                );
            }


            if (employe.salario > employeWithSameLastNameWhoIncomesMore.salary)
            {
                employeWithSameLastNameWhoIncomesMore.salary = employe.salario;
                employeWithSameLastNameWhoIncomesMore.employees.Clear();
                employeWithSameLastNameWhoIncomesMore.employees.Add(employe);
            }
            else
            if (employe.salario == employeWithSameLastNameWhoIncomesMore.salary)
            {
                employeWithSameLastNameWhoIncomesMore.employees.Add(employe);
            }

            employeWithSameLastNameWhoIncomesMore.numberOfEmployees++;
            employeesWithSameLastNameWhoIncomesMore[employe.sobrenome] = employeWithSameLastNameWhoIncomesMore;


            #endregion
        }

        private void areasHandler(Areas area)
        {
            this.areas.Add(area.codigo, area.nome);
        }
    }

    public class Funcionario
    {
        public string FullName => this.nome + " " + this.sobrenome;

        public int id { get; set; }
        public string nome { get; set; }
        public string sobrenome { get; set; }
        public string area { get; set; }
        public float salario { get; set; }

        public override string ToString()
        {
            return
    $@"{{ 
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

