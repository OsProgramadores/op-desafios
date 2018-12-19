using System.Collections.Generic;

namespace Desafio5
{
    public class AreaStats
    {
        public int Code { get; set; }
        public double Salario { get; set; }
        public int TotalFuncionarios { get; set; }
        public double MinSalario { get; set; }
        public double MaxSalario { get; set; }
        public List<FullName> Max { get; set; }
        public List<FullName> Min { get; set; }
    }
}