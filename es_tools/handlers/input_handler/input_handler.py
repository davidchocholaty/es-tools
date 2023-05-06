"""Implementace nástroje pro práci se vstupními soubory.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje nástroj pro práci se vstupními soubory, který využívají všechny implementované nástroje v rámci
aplikací nového formálního systému.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: input_handler.py
"""

import sys

from typing import Union, TextIO, IO

from es_tools.handlers.handler import Handler


class InputHandler(Handler):
    """Zpracování vstupního souboru.

    Metody této třídy implementují zpracování vstupního souboru a načtení samotných vstupních dat.
    """
    def __init__(self, source: str) -> None:
        """**Konstruktor třídy InputHandler**

        Konstruktor slouží pro samotné načtení vstupních dat ze vstupního souboru, jehož umístení je zadáno v rámci
        parametru source.

        :param source: vstupní soubor.
        :type source: str
        :raises OSError: chyba při otevření souboru (soubor neexistuje, jedná se o adresář, ...).
        """
        if source:
            try:
                self.__source_handler = open(source, "r")
            except OSError:
                raise
        else:
            self.__source_handler = sys.stdin

    def handler(self) -> Union[TextIO, IO]:
        """Navrácení manipulátoru pro práci se vstupním tokem dat.

        :return: manipulátor s proudem dat ze vstupního souboru (IO) nebo ze standardního vstupu (TextIO).
        :rtype: Union[TextIO, IO]
        """
        return self.__source_handler


def create_input_handler(input_file: str) -> InputHandler:
    """Funkce pro vytvoření manipulátoru se vstupním tokem dat.

    Tato funkce slouží především pro vytvoření instance třídy InputHandler obsahující manipulátor pro práci se vstupním
    tokem dat.

    :param input_file: umístení vstupního souboru včetně jeho názvu.
    :type input_file: str
    :return: instance třídy InputHandler obsahující samotný manipulátor.
    :rtype: InputHandler
    :raises OSError: chyba při otevření souboru (soubor neexistuje, jedná se o adresář, ...).
    """
    try:
        file_handler = InputHandler(input_file)
    except OSError:
        raise

    return file_handler
