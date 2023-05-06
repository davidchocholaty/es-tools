"""Abtraktní třída pro nástroj.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje abstraktní třídu, která je bázovou třídou pro všechny nástroje implementující jednotlivé aplikace
vymazávacího systému, jejichž třídy jsou zděděny od této třídy.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: tool.py
"""
import argparse

from abc import ABC, abstractmethod

from es_tools.custom_exceptions.internal_error_exception import InternalErrorException
from es_tools.custom_exceptions.invalid_input_data_structure_exception import InvalidInputDataStructure
from es_tools.handlers.argument_handler.argument_handler import ArgumentHandler
from es_tools.handlers.input_handler.input_handler import create_input_handler


class Tool(ABC):
    """Základní třída pro nástroje implementující aplikace vymazávacího systému.

    Tato abstraktní třída se využívá jako kořenová třída pro všechny nástroje, které dědí od této třídy. Významnými
    metodami, které obsahuje, jsou abstraktní metody _initialize_tool() a run(). Metoda _initialize_tool() slouží
    pro inicializaci nástroje a metoda run() sjednocuje rozhraní nástrojů pro spuštění jejich vlastní funkcionality.
    """
    def __init__(self, input_lines_number: int = -1) -> None:
        """**Kontruktor třídy Tool**

        Konstruktor slouží pouze pro nastavení základních hodnot atributů třídy, přičemž především je nastavena hodnota
        určující očekávaný počet vstupních řádků ve vstupním souboru pro daný nástroj, jehož třída je odvozena od této
        třídy.

        :param input_lines_number: očekávaný počet řádků ve vstupním souboru (hodnota -1 značí neomezený počet).
        :type input_lines_number: int
        """
        self.arguments = None
        self.input_data = None
        self.input_lines_number = input_lines_number

    def get_tool_name(self) -> str:
        """Získání názvu nástroje.

        :return: název nástroje.
        :rtype: str
        """
        return self.__class__.__name__

    def print_tool_name(self) -> None:
        """Metoda sloužící pro výpis názvu nástroje na standardní výstup."""
        tool_name = self.__class__.__name__
        border = "-" * len(tool_name)

        print(border)
        print(tool_name)
        print(border)

    def load_input_data(self) -> None:
        """Načtení dat ze vstupního souboru.

        Tato fundamentální metoda abstraktní třídy Tool slouží pro vytvoření manipulátoru pro práci se vstupním
        souborem, přičemž pokud je to možné, jsou zároveň načtena vstupní data.

        :raises InternalErrorException: neočekávaný výskyt interní chyby programu.
        :raises InvalidInputDataStructure: neplatná struktura vstupních dat.
        :raises OSError: chyba při pokusu o načtení vstupních dat ze souboru (soubor neexistuje, jedná se o adresář,
                        ...).
        """
        if self.arguments is None:
            raise InternalErrorException

        # Load input data.
        try:
            input_handler = create_input_handler(self.arguments.input)
        except OSError:
            raise

        input_data = input_handler.handler().readlines()

        # Následující řádek kódu je převzat:
        #
        # Zdrojový web: Stack Overflow.
        # Odkaz na původní otázku: https://stackoverflow.com/questions/7984169/remove-trailing-newline-from-the-elements-of-a-string-list
        # Autor otázky: George Burrows (https://stackoverflow.com/users/1015156/george-burrows).
        # Otázka upravena: Eugene Yarmash (https://stackoverflow.com/users/244297/eugene-yarmash).
        # Autor odpovědi: Sven Marnach (https://stackoverflow.com/users/279627/sven-marnach).
        #
        # *** Začátek převzatého kódu. ***
        input_data = [line.strip() for line in input_data]
        # *** Konec převzatého kódu. ***

        if "" in input_data:
            input_data.remove("")

        if self.input_lines_number != -1 and (len(input_data) > self.input_lines_number or len(input_data) < 1):
            raise InvalidInputDataStructure

        self.input_data = input_data

    def _load_arguments(self) -> None:
        """Metoda pro načtení uživatelských argumentů.

        Hlavním cílem této metody je sjednotit soukromé metody pro implementované nástroje, přičemž její implementace
        není zcela striktně vyžadována, pokud by nástroj nepožadoval pro svou funkcionalitu žádné uživatelské parametry.
        """
        pass

    def _add_custom_arguments(self, argument_handler: argparse.ArgumentParser) -> None:
        """Metoda pro přidání specifických uživatelských argumentů pro daný nástroj.

        Hlavním cílem této metody je sjednotit soukromé metody pro implementované nástroje, přičemž její implementace
        není zcela striktně vyžadována, pokud by nástroj nevyužíval specifické uživatelské argumenty.

        :param argument_handler: analyzátor uživatelských argumentů.
        :type argument_handler: argparse.ArgumentParser
        """
        pass

    def _create_custom_argument_handler(self) -> ArgumentHandler:
        """Metoda pro vytvoření manipulátoru s uživatelskými argumenty.

        Metoda pro vytvoření manipulátoru s uživatelskými argumenty, přičemž ke společným argumentům jsou přidány
        i specifické pro daný nástroj. Hlavním cílem této metody je sjednotit soukromé metody pro implementované
        nástroje, přičemž její implementace není zcela striktně vyžadována, pokud by nástroj pro svou funkcionalitu
        nepožadoval žádné uživatelské argumenty.

        :return: manipulátor s uživatelskými argumenty.
        :rtype: ArgumentHandler
        """
        pass

    @abstractmethod
    def _run_main_algorithm(self) -> None:
        """Abstraktní metoda reprezentující metody pro spuštení hlavního algoritmu příslušného nástroje.

        Hlavním cílem této metody je sjednotit soukromé funkce pro implementované nástroje, přičemž její implementace
        je striktně vyžadována.
        """
        pass

    @abstractmethod
    def _initialize_tool(self) -> None:
        """Abstraktní metoda reprezentující metodu pro inicializaci nástroje.

        Tato abstraktní metoda reprezentuje metodu pro inicializaci nástroje, to znamená pro načtení vstupních dat
        ze souboru a zpracování uživatelských argumentů.
        """
        pass

    @abstractmethod
    def run(self) -> None:
        """Abstraktní metoda reprezentující metodu pro spuštění funkcionality nástoje.

        Tato abstraktní metoda reprezentuje metodu pro spuštění samotného algoritmu a funkcionality nástroje. Cílem
        této metody je sjednotit rozhraní pro všechny implementované nástroje.
        """
        pass
