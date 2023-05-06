"""Skript pro spuštení ukázkového příkladu pro demonstraci funkcionality nástroje pro vlastnosti sekundární
struktury RNA.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje implementaci pomocného nástroje pro spuštění jednotlivých ukázkových příkladů implementovaného
nástroje reprezentujícího aplikaci vymazávacího systému pro ověření vlastností sekundární struktury RNA.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: run_example_secondary_structure_properties_tool.py
"""

from os import path as ospath

from es_tools.custom_exceptions.invalid_example_number_exception import InvalidExampleNumberException
from es_tools.custom_exceptions.unknown_platform_system_exception import UnknownPlatformSystemException
from es_tools.examples.custom_utils.run_tool import run_tool
from es_tools.examples.custom_utils.set_python_command_os_type import set_python_command_os_type


def run_example_secondary_structure_properties_tool(no_install_run: bool,
                                                    example_number: int,
                                                    verbose: bool,
                                                    greedy_quantifier: bool) -> None:
    """Spuštění příkladu pro prezentaci ukázkového příkladu nástroje pro vlastnosti sekundární struktury RNA.

    Tato funkce pomocí podprocesu spustí vytvořený ukázkový příklad pro demonstraci funkcionality nástroje
    pro ověření vlastností sekundární struktury RNA.

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

    tool_path = ospath.join("es_tools", "tools", "secondary_structure_properties_tool", "secondary_structure_properties_tool.py")
    data_path = ospath.join("es_tools", "examples", "secondary_structure_properties_tool", "data")

    match example_number:
        case 1:
            # python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py
            #     -i es_tools/examples/secondary_structure_properties_tool/data/1_min_accepted.txt --min 60
            command = command + tool_path + " -i " + ospath.join(data_path, "1_min_accepted.txt") + " --min 60"
        case 2:
            # python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py
            #     -i es_tools/examples/secondary_structure_properties_tool/data/2_min_not_accepted.txt --min 80
            command = command + tool_path + " -i " + ospath.join(data_path, "2_min_not_accepted.txt") + " --min 80"
        case 3:
            # python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py
            #     -i es_tools/examples/secondary_structure_properties_tool/data/3_max_accepted.txt --max 60
            command = command + tool_path + " -i " + ospath.join(data_path, "3_max_accepted.txt") + " --max 60"
        case 4:
            # python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py
            #     -i es_tools/examples/secondary_structure_properties_tool/data/4_max_not_accepted.txt --max 50
            command = command + tool_path + " -i " + ospath.join(data_path, "4_max_not_accepted.txt") + " --max 50"
        case 5:
            # python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py
            #     -i es_tools/examples/secondary_structure_properties_tool/data/5_both_accepted.txt --min 60 --max 80
            command = command + tool_path + " -i " + ospath.join(data_path, "5_both_accepted.txt") + \
                      " --min 60 --max 80"
        case 6:
            # python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py
            #     -i es_tools/examples/secondary_structure_properties_tool/data/6_both_not_accepted_below.txt
            #     --min 80 --max 90
            command = command + tool_path + " -i " + ospath.join(data_path, "6_both_not_accepted_below.txt") + \
                      " --min 80 --max 90"
        case 7:
            # python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py
            #     -i es_tools/examples/secondary_structure_properties_tool/data/7_both_not_accepted_above.txt
            #     --min 20 --max 40
            command = command + tool_path + " -i " + ospath.join(data_path, "7_both_not_accepted_above.txt") + \
                      " --min 20 --max 40"
        case 8:
            # python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py
            #     -i es_tools/examples/secondary_structure_properties_tool/data/8_default_min_max_levels.txt
            command = command + tool_path + " -i " + ospath.join(data_path, "8_default_min_max_levels.txt")
        case 9:
            # python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py
            #     -i es_tools/examples/secondary_structure_properties_tool/data/9_min_rounded_accepted.txt --min 57
            command = command + tool_path + " -i " + ospath.join(data_path, "9_min_rounded_accepted.txt") + " --min 57"
        case 10:
            # python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py
            #     -i es_tools/examples/secondary_structure_properties_tool/data/10_max_rounded_accepted.txt --max 71
            command = command + tool_path + " -i " + ospath.join(data_path, "10_max_rounded_accepted.txt") + " --max 71"
        case 11:
            # python3 es_tools/tools/secondary_structure_properties_tool/secondary_structure_properties_tool.py
            #     -i es_tools/examples/secondary_structure_properties_tool/data/11_both_rounded_accepted.txt
            #     --min 57 --max 91
            command = command + tool_path + " -i " + ospath.join(data_path, "11_both_rounded_accepted.txt") + \
                      " --min 57 --max 91"
        case other:
            command = ""

    try:
        run_tool(no_install_run, command, verbose, greedy_quantifier)
    except InvalidExampleNumberException:
        raise
