"""Zpracování uživatelských argumentů.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje implementaci zpracování uživatelských argumentů, přičemž definuje společné základní argumenty
a obsahuje metodu pro samotné načtení vstupních uživatelských parametrů.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: argument_handler.py
"""

import argparse

from typing import Any

from es_tools.custom_exceptions.invalid_argument_exception import InvalidArgumentException
from es_tools.handlers.argument_handler.argument_parser import ArgumentParser
from es_tools.handlers.handler import Handler


class ArgumentHandler(Handler):
    """Nástroj pro zpracování uživatelských argumentů.

    Metody této třídy implementují nástroj pro zpracování vstupních uživatelských argumentů, přičemž jsou nastaveny
    společné vstupní argumenty a je poskytnuta metoda pro samotnou analýzu všech (i specifických) argumentů.
    """
    def __init__(self, tool_name: str) -> None:
        """**Konstruktor třídy ArgumentHandler**

        Konstruktor slouží především pro vytvoření samotného analyzátoru argumentů a pro nastavení společných
        uživatelských argumentů.

        :param tool_name: název nástroje implementujícího aplikací nového formálního systému.
        :type tool_name: str
        """
        self.__parser = ArgumentParser(prog=tool_name)

        self.__parser.add_argument("-v", "--verbose", dest="verbose", action="store_true",
                                   help="if set, the used erasing strings, the current input tape shape and "
                                        "the current string shape created by concatenating the erasing strings "
                                        "will be printed")
        self.__parser.add_argument("-l", "--lazy", dest="greedy_quantifier", action="store_false",
                                   help="if set, the lazy quantifier type for the used erasing system(s) is used. "
                                        "By default, the greedy quantifier type is used")

    def parse_arguments(self) -> Any:
        """Analýza uživatelských argumentů.

        Tato funkce slouží pro provedení analýzy (zadaných) uživatelských argumentů.

        :return: navrací uživatelské argumenty.
        :rtype: Any
        :raises InvalidArgumentException: zadání neplatného uživatelského argumentu.
        """
        arguments, leftovers = self.__parser.parse_known_args()

        # Neznámý vstupní argument.
        if len(leftovers) > 0:
            raise InvalidArgumentException

        return arguments

    def handler(self) -> argparse.ArgumentParser:
        """Získání analyzátoru argumentů.

        :return: navrací analyzátor argumentů.
        :rtype: argparse.ArgumentParser
        """
        return self.__parser
