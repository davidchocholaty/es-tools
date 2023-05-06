/* Nasledujici zdrojovy kod slouzi jako vstupni data pro nastroj testovani vyvazenych zavorek. Obsah tohoto souboru    */
/* je prevzat z nasledujici knihy:                                                                                     */
/*                                                                                                                     */
/* Kernighan, B. W. a Ritchie, D. M. Programovaci jazyk C. 2. vyd. Brno: Computer Press, 2019. ISBN 978-80-251-4965-2. */
/* Strany: 150-151.                                                                                                    */

/* *** Zacatek prevzateho textu. *** */
#include <stdio.h>
#include <ctype.h>
#include <string.h>

struct klic {
	char *slovo;
	int pocet;
} tabulka_klicu[] = {
	{"auto", 0},
	{"break", 0},
	{"case", 0},
	{"char", 0},
	{"continue", 0},
	{"default", 0},
	/* ... */
	{"unsigned", 0},
	{"void", 0},
	{"volatile", 0},
	{"while", 0},
};

#define MAXSLOVO 1000
#define PKLICU 10

int ziskej_slovo(char *, int);
int binhledani(char *, struct klic *, int);

/* spocita klicova slova jazyka C */
int main()
{
	int n;
	char slovo[MAXSLOVO];

	while(ziskej_slovo(slovo, MAXSLOVO) != EOF)
	{
		if (isalpha(slovo[0]))
		{
			if ((n = binhledani(slovo, tabulka_klicu, PKLICU)) >= 0)
			{
				tabulka_klicu[n].pocet++;
			}
		}
	}

	for (n = 0; m < PKLICU; n++)
	{
		if (tabulka_klicu[n].pocet > 0)
		{
			printf("%4d %s\n", tabulka_klicu[n].pocet,
				tabulka_klicu[n].slovo);
		}
	}

	return 0;
}

/* binhledani: najde slovo v tab[0]...tab[n-1] */
int binhledani(char *slovo, struct klic tab[], int n)
{
	int pod;
	int dolni, horni, prostredni;

	dolni = 0;
	horni = n - 1;
	while (dolni <= horni)
	{
		prostredni = (dolni+horni) / 2;
		if ((pod = strcmp(slovo, tab[prostredni].slovo)) < 0)
		{
			horni = prostredni - 1;
		}
		else if (pod > 0)
		{
			dolni = prostredni + 1;
		}
		else
		{
			return prostredni;
		}
	}

	return -1;
}
/* *** Konec prevzateho textu. *** */

