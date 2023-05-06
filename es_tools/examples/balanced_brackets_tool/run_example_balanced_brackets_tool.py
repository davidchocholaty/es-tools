"""Skript pro spuštení ukázkového příkladu pro demonstraci funkcionality nástroje pro vyvážené závorky.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje implementaci pomocného nástroje pro spuštění jednotlivých ukázkových příkladů implementovaného
nástroje reprezentujícího aplikaci vymazávacího systému pro vyvážené závorky v textových editorech.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: run_example_balanced_brackets_tool.py
"""

from os import path as ospath

from es_tools.custom_exceptions.invalid_example_number_exception import InvalidExampleNumberException
from es_tools.custom_exceptions.unknown_platform_system_exception import UnknownPlatformSystemException
from es_tools.examples.custom_utils.run_tool import run_tool
from es_tools.examples.custom_utils.set_python_command_os_type import set_python_command_os_type


def run_example_balanced_brackets_tool(no_install_run: bool,
                                       example_number: int,
                                       verbose: bool,
                                       greedy_quantifier: bool) -> None:
    """Spuštění příkladu pro prezentaci ukázkového příkladu nástroje pro vyvážené závorky.

    Tato funkce pomocí podprocesu spustí vytvořený ukázkový příklad pro demonstraci funkcionality nástroje
    pro vyvážené závorky.

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

    tool_path = ospath.join("es_tools", "tools", "balanced_brackets_tool", "balanced_brackets_tool.py")
    data_path = ospath.join("es_tools", "examples", "balanced_brackets_tool", "data")

    match example_number:
        case 1:
            # python3 es_tools/tools/balanced_brackets_tool/balanced_brackets_tool.py
            #     -i es_tools/examples/balanced_brackets_tool/data/1_c_hello_world.c
            command = command + tool_path + " -i " + ospath.join(data_path, "1_c_hello_world.c")
        case 2:
            # python3 es_tools/tools/balanced_brackets_tool/balanced_brackets_tool.py
            #     -i es_tools/examples/balanced_brackets_tool/data/2_c_complex.c
            command = command + tool_path + " -i " + ospath.join(data_path, "2_c_complex.c")
        case 3:
            # python3 es_tools/tools/balanced_brackets_tool/balanced_brackets_tool.py
            #     -i es_tools/examples/balanced_brackets_tool/data/3_cpp_example.cpp
            command = command + tool_path + " -i " + ospath.join(data_path, "3_cpp_example.cpp")
        case 4:
            # python3 es_tools/tools/balanced_brackets_tool/balanced_brackets_tool.py
            #     -i es_tools/examples/balanced_brackets_tool/data/4_plain_text_1_correct.txt
            command = command + tool_path + " -i " + ospath.join(data_path, "4_plain_text_1_correct.txt")
        case 5:
            # python3 es_tools/tools/balanced_brackets_tool/balanced_brackets_tool.py
            #     -i es_tools/examples/balanced_brackets_tool/data/5_plain_text_2_correct.txt
            command = command + tool_path + " -i " + ospath.join(data_path, "5_plain_text_2_correct.txt")
        case 6:
            # python3 es_tools/tools/balanced_brackets_tool/balanced_brackets_tool.py
            #     -i es_tools/examples/balanced_brackets_tool/data/6_plain_text_3_incorrect.txt
            command = command + tool_path + " -i " + ospath.join(data_path, "6_plain_text_3_incorrect.txt")
        case 7:
            # python3 es_tools/tools/balanced_brackets_tool/balanced_brackets_tool.py
            #     -i es_tools/examples/balanced_brackets_tool/data/7_plain_text_4_incorrect.txt
            command = command + tool_path + " -i " + ospath.join(data_path, "7_plain_text_4_incorrect.txt")
        case 8:
            # python3 es_tools/tools/balanced_brackets_tool/balanced_brackets_tool.py
            #     -i es_tools/examples/balanced_brackets_tool/data/8_all_bracket_types_correct.txt
            command = command + tool_path + " -i " + ospath.join(data_path, "8_all_bracket_types_correct.txt")
        case 9:
            # python3 es_tools/tools/balanced_brackets_tool/balanced_brackets_tool.py
            #     -i es_tools/examples/balanced_brackets_tool/data/9_all_bracket_types_incorrect.txt
            command = command + tool_path + " -i " + ospath.join(data_path, "9_all_bracket_types_incorrect.txt")
        case 10:
            # python3 es_tools/tools/balanced_brackets_tool/balanced_brackets_tool.py
            #     -i es_tools/examples/balanced_brackets_tool/data/10_illegal_character_occurrence.txt
            command = command + tool_path + " -i " + ospath.join(data_path, "10_illegal_character_occurrence.txt")
        case other:
            command = ""

    try:
        run_tool(no_install_run, command, verbose, greedy_quantifier)
    except InvalidExampleNumberException:
        raise
