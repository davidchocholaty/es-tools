"""Skript pro spuštení ukázkového příkladu pro demonstraci funkcionality nástroje pro ověření správnosti řešení
problému n dam.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje implementaci pomocného nástroje pro spuštění jednotlivých ukázkových příkladů implementovaného
nástroje reprezentujícího aplikaci vymazávacího systému pro ověření správnosti řešení problému n dam.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: run_example_n_queens_problem_tool.py
"""
import os
from os import path as ospath

from es_tools.custom_exceptions.invalid_example_number_exception import InvalidExampleNumberException
from es_tools.custom_exceptions.unknown_platform_system_exception import UnknownPlatformSystemException
from es_tools.examples.custom_utils.run_tool import run_tool
from es_tools.examples.custom_utils.set_python_command_os_type import set_python_command_os_type


def run_example_n_queens_problem_tool(no_install_run: bool,
                                      example_number: int,
                                      verbose: bool,
                                      greedy_quantifier: bool) -> None:
    """Spuštění příkladu pro prezentaci ukázkového příkladu nástroje pro ověření správnosti řešení problému n dam.

    Tato funkce pomocí podprocesu spustí vytvořený ukázkový příklad pro demonstraci funkcionality nástroje
    pro ověření správnosti řešení problému n dam.

    :param no_install_run: spuštění nástroje v režimu bez instalace balíčku.
    :type no_install_run: bool
    :param example_number: číslo spouštěného příkladu.
    :type example_number: int
    :param verbose: určení, zda mají být vypisovány na standardní výstup při činnosti vymazávacího systému podrobné
                    informace.
    :type verbose: bool
    :param greedy_quantifier: typ kvantifikátoru (True — chamtivý, False — líný).
    :type greedy_quantifier: bool
    :raises InvalidExampleNumberException: číslo spouštěného rozsahu mimo příslušný rozsah.
    :raises UnknownPlatformSystemException: neznámý operační systém.
    """
    try:
        command = set_python_command_os_type()
    except UnknownPlatformSystemException:
        raise

    tool_path = ospath.join("es_tools", "tools", "n_queens_problem_tool", "n_queens_problem_tool.py")
    data_path = ospath.join("es_tools", "examples", "n_queens_problem_tool", "data")

    match example_number:
        case 1:
            # python3 es_tools/tools/n_queens_problem_tool/n_queens_problem_tool.py
            #     -i es_tools/examples/n_queens_problem_tool/data/1_n_8_correct.txt -n 8
            command = command + tool_path + " -i " + ospath.join(data_path, "1_n_8_correct.txt") + " -n 8"
        case 2:
            # python3 es_tools/tools/n_queens_problem_tool/n_queens_problem_tool.py
            #     -i es_tools/examples/n_queens_problem_tool/data/2_n_8_incorrect_horizontal.txt -n 8
            command = command + tool_path + " -i " + ospath.join(data_path, "2_n_8_incorrect_horizontal.txt") + " -n 8"
        case 3:
            # python3 es_tools/tools/n_queens_problem_tool/n_queens_problem_tool.py
            #     -i es_tools/examples/n_queens_problem_tool/data/3_n_8_incorrect_right_diagonal.txt -n 8
            command = command + tool_path + " -i " + ospath.join(data_path, "3_n_8_incorrect_right_diagonal.txt") + \
                      " -n 8"
        case 4:
            # python3 es_tools/tools/n_queens_problem_tool/n_queens_problem_tool.py
            #     -i es_tools/examples/n_queens_problem_tool/data/4_n_8_multiple_incorrectness.txt -n 8
            command = command + tool_path + " -i " + ospath.join(data_path, "4_n_8_multiple_incorrectness.txt") + \
                      " -n 8"
        case 5:
            # python3 es_tools/tools/n_queens_problem_tool/n_queens_problem_tool.py
            #     -i es_tools/examples/n_queens_problem_tool/data/5_n_4_correct.txt -n 4
            command = command + tool_path + " -i " + ospath.join(data_path, "5_n_4_correct.txt") + " -n 4"
        case 6:
            # python3 es_tools/tools/n_queens_problem_tool/n_queens_problem_tool.py
            #     -i es_tools/examples/n_queens_problem_tool/data/6_n_4_incorrect_horizontal.txt -n 4
            command = command + tool_path + " -i " + ospath.join(data_path, "6_n_4_incorrect_horizontal.txt") + " -n 4"
        case 7:
            # python3 es_tools/tools/n_queens_problem_tool/n_queens_problem_tool.py
            #     -i es_tools/examples/n_queens_problem_tool/data/7_n_4_incorrect_vertical.txt -n 4
            command = command + tool_path + " -i " + ospath.join(data_path, "7_n_4_incorrect_vertical.txt") + " -n 4"
        case 8:
            # python3 es_tools/tools/n_queens_problem_tool/n_queens_problem_tool.py
            #     -i es_tools/examples/n_queens_problem_tool/data/8_n_4_incorrect_both_diagonal.txt -n 4
            command = command + tool_path + " -i " + ospath.join(data_path, "8_n_4_incorrect_both_diagonal.txt") + \
                      " -n 4"
        case 9:
            # python3 es_tools/tools/n_queens_problem_tool/n_queens_problem_tool.py
            #     -i es_tools/examples/n_queens_problem_tool/data/9_n_12_correct.txt -n 12
            command = command + tool_path + " -i " + ospath.join(data_path, "9_n_12_correct.txt") + " -n 12"
        case 10:
            # python3 es_tools/tools/n_queens_problem_tool/n_queens_problem_tool.py
            #     -i es_tools/examples/n_queens_problem_tool/data/10_n_12_incorrect_vertical.txt -n 12
            command = command + tool_path + " -i " + ospath.join(data_path, "10_n_12_incorrect_vertical.txt") + " -n 12"
        case 11:
            # python3 es_tools/tools/n_queens_problem_tool/n_queens_problem_tool.py
            #     -i es_tools/examples/n_queens_problem_tool/data/11_n_12_incorrect_left_diagonal.txt -n 12
            command = command + tool_path + " -i " + ospath.join(data_path, "11_n_12_incorrect_left_diagonal.txt") + \
                      " -n 12"
        case other:
            command = ""

    try:
        run_tool(no_install_run, command, verbose, greedy_quantifier)
    except InvalidExampleNumberException:
        raise
