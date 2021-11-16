using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Project명
namespace Giraffe
{
    class Program
    {
        static void Main(string[] args) // Main is function!
        {
            Console.Write("Enter a number: ");
            int num1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(num1);
            Console.ReadLine();
        }
    }
}