using System;
using Newtonsoft.Json;
using System.Linq;
using System.Collections.Generic;

namespace desafio5
{
    class Areas
    {
        public string codigo { get; set; }
        public string nome { get; set; }
    }

    class Funcionarios
    {
        public int id { get; set; }
        public string nome { get; set; }
        public string sobrenome { get; set; }
        public decimal salario { get; set; }
        public string area { get; set; }
        public Areas Area { get; set; }
    }

    class Json
    {
        public List<Funcionarios> funcionarios { get; set; }
        public List<Areas> areas { get; set; }
    }


    class Program
    {
        static void Main(string[] args)
        {
            string json;
            using (var sw = new System.IO.StreamReader("funcionarios.json"))
            {
                json = sw.ReadToEnd();
            }

            var obj = JsonConvert.DeserializeObject<Json>(json);

            var funcionarios = obj.funcionarios;
            var areas = obj.areas;

            funcionarios.ForEach(funcionario => funcionario.Area = areas.First(x => x.codigo == funcionario.area));


            var quemMaisRecebe = funcionarios.Max(x => x.salario);
            var quemMenosRecebe = funcionarios.Min(x => x.salario);
            var mediaSalarialDaEmpresa = funcionarios.Average(x => x.salario);

            ImprimirBlocoRecebimentos(quemMaisRecebe, quemMenosRecebe, mediaSalarialDaEmpresa);

            var gruposFuncionarios = funcionarios.GroupBy(x => x.Area);

            var quantidadeDeFuncionariosPorArea = new Dictionary<Areas, int>();
            foreach (var grupo in gruposFuncionarios)
            {
                quantidadeDeFuncionariosPorArea[grupo.Key] = grupo.Count();


                Console.WriteLine();
                ImprimirArea("Gupo {0}:{1}", grupo.Key);
                var funcionariosDesseGrupo = grupo.ToList();
                quemMaisRecebe = funcionariosDesseGrupo.Max(x => x.salario);
                quemMenosRecebe = funcionariosDesseGrupo.Min(x => x.salario);
                mediaSalarialDaEmpresa = funcionariosDesseGrupo.Average(x => x.salario);

                ImprimirBlocoRecebimentos(quemMaisRecebe, quemMenosRecebe, mediaSalarialDaEmpresa);
            }
            Console.WriteLine();

            var areaComMaisFuncionarios = quantidadeDeFuncionariosPorArea.First(x => x.Value == quantidadeDeFuncionariosPorArea.Values.Max()).Key;
            var areaComMenosFuncionarios = quantidadeDeFuncionariosPorArea.First(x => x.Value == quantidadeDeFuncionariosPorArea.Values.Min()).Key;
            ImprimirArea("Area com mais funcionarios {0}:{1}", areaComMaisFuncionarios);
            ImprimirArea("Area com menos funcionarios {0}:{1}", areaComMenosFuncionarios);

            Console.WriteLine();

            var funcionariosComMesmoSobrenome =
                from f in funcionarios
                group f by f.sobrenome into g
                let total = g.Count()
                where total >= 2
                select g;

            Console.WriteLine("Funcionários com o mesmo sobrenome com maiores salários");
            foreach (var f in funcionariosComMesmoSobrenome)
            {
                var funcionarioComMaiorSalario = f.First(x => x.salario == f.Max(y => y.salario));

                Console.WriteLine("\t {0}: {1} {2} - {3}",
                 funcionarioComMaiorSalario.id,
                 funcionarioComMaiorSalario.nome,
                 funcionarioComMaiorSalario.sobrenome,
                 funcionarioComMaiorSalario.salario
                 );
            }
        }

        private static void ImprimirArea(string msg, Areas area)
        {
            Console.WriteLine(msg, area.codigo, area.nome);
        }

        private static void ImprimirBlocoRecebimentos(decimal quemMaisRecebe, decimal quemMenosRecebe, decimal mediaSalarialDaEmpresa)
        {
            ImprimirQuemMaisRecebe(quemMaisRecebe);
            ImprimirQuemMenosRecebe(quemMenosRecebe);
            ImprimirMediaSalarial(mediaSalarialDaEmpresa);
        }

        private static void ImprimirMediaSalarial(decimal mediaSalarialDaEmpresa)
        {
            Console.WriteLine("Média salárial {0}", mediaSalarialDaEmpresa);
        }

        private static void ImprimirQuemMenosRecebe(decimal quemMenosRecebe)
        {
            Console.WriteLine("Menor salário {0}", quemMenosRecebe);
        }

        private static void ImprimirQuemMaisRecebe(decimal quemMaisRecebe)
        {
            Console.WriteLine("Maior salário {0}", quemMaisRecebe);
        }
    }
}
