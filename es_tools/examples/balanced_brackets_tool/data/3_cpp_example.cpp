/* Nasledujici zdrojovy kod slouzi jako vstupni data pro nastroj testovani vyvazenych zavorek. Obsah tohoto souboru    */
/* byl prevzat z nasledujici knihy:                                                                                    */
/*                                                                                                                     */
/* Stroustrup, B. The C++ Programming Language: Fourth Edition. 4. vyd. Ann Arbor: Addison-Wesley, 2013. 1346 s.       */
/* ISBN 978-0-321-56384-2.                                                                                             */
/* Strany: 39-40.                                                                                                      */

/* *** Zacatek prevzateho textu. *** */
#include <iostream>
using namespace std;

double square(double x)
{
	return x*x;
}

void print_square(double x)
{
	cout << "the square of " << x << " is " << square(x) << "\n";
}

int main()
{
	print_square(1.234);
}
/* *** Konec prevzateho textu. *** */

