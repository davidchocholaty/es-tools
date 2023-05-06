"""Spuštění nástroje pomocí konkrétního příkazu s využitím podprocesu.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci, která s využitím podprocesu spustí již konkrétní ukázkový příklad pro specifický nástroj.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: run_tool.py
"""
import os
from subprocess import call

from definitions import ROOT_DIRECTORY
from es_tools.custom_exceptions.invalid_example_number_exception import InvalidExampleNumberException
from es_tools.examples.custom_utils.add_package_path_for_subprocess_call import add_package_path_for_subprocess_call


def run_tool(no_install_run: bool, command: str, verbose: bool, greedy_quantifier: bool) -> None:
    """Spuštění specifického nástroje pro konkrétní příklad.

    :param no_install_run: spuštění nástroje v režimu bez instalace balíčku.
    :type no_install_run: bool
    :param command: příkaz pro spuštění ukázkového příkladu.
    :type command: str
    :param verbose: určení, zda mají být vypisovány na standardní výstup při činnosti vymazávacího systému podrobné
                    informace.
    :type verbose: bool
    :param greedy_quantifier: typ kvantifikátoru (True — chamtivý, False — líný).
    :type greedy_quantifier: bool
    :raises InvalidExampleNumberException: číslo spouštěného příkladu mimo příslušný rozsah.
    """
    if verbose:
        command = command + " -v"

    if not greedy_quantifier:
        command = command + " -l"

    if command:
        print("Running command: " + command + "\n")

        # Změna aktuálního pracovního adresáře na kořenový adresář projektu. Tato změna je nutná z ohledu
        # odpovídajícího umístění souborů pro hierarchickou adresářovou strukturu využitou ve volaných příkazech.
        os.chdir(ROOT_DIRECTORY)

        if no_install_run:
            add_package_path_for_subprocess_call()

        return_code = call(command, shell=True)

        print("####################################################################################\n")
        print("\nReturn code: " + str(return_code))
    else:
        raise InvalidExampleNumberException
