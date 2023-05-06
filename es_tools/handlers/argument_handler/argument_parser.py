"""Analyzátor argumentů.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje analyzátor argumentů, přičemž slouží především pro vlastní zpracování chybových stavů.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: argument_parser.py
"""

import argparse

from es_tools.error_utils.exit_code import ExitCode


class ArgumentParser(argparse.ArgumentParser):
    """Analyzátor argumentů.

    Metody této třídy implementují analyzátor uživatelských argumentů. Hlavním cílem této třídy je implementace metody
    přepisující funkcionalitu stejnojmenné metody rodičovské třídy argparse.ArgumentParser pro zpracování chybových
    stavů při zpracování vstupních argumentů. Motivací vytvoření příslušné třídy je zadání vlastního tvaru výpisu
    chybové zprávy a ukončení programu s vlastním chybovým kódem.
    """
    def error(self, error_message):
        """Výpis chybové zprávy pro zpracování argumentů a ukončení programu s chybovým kódem.

        Tato metoda přepisuje stejnojmennou metodu rodičovské třídy argparse.ArgumentParser, přičemž je nastaven
        vlastní tvar výpisu chybové zprávy a zvolen vlastní chybový kód pro ukončení programu.

        :param error_message: chybová zpráva.
        :type error_message: Any
        """
        print("\nError: " + error_message + ".")
        self.exit(ExitCode.WRONG_ARGUMENT.value)
