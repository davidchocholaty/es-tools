"""Skript pro spuštení ukázkového příkladu pro demonstraci funkcionality nástroje pro vyhledávání sekvencí.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje implementaci pomocného nástroje pro spuštění jednotlivých ukázkových příkladů implementovaného
nástroje reprezentujícího aplikaci vymazávacího systému pro vyhledávání sekvencí.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: run_example_sequence_sequence_search_tool.py
"""

from os import path as ospath

from es_tools.custom_exceptions.invalid_example_number_exception import InvalidExampleNumberException
from es_tools.custom_exceptions.unknown_platform_system_exception import UnknownPlatformSystemException
from es_tools.examples.custom_utils.run_tool import run_tool
from es_tools.examples.custom_utils.set_python_command_os_type import set_python_command_os_type


def run_example_sequence_search_tool(no_install_run: bool,
                                     example_number: int,
                                     verbose: bool,
                                     greedy_quantifier: bool) -> None:
    """Spuštění příkladu pro prezentaci ukázkového příkladu nástroje pro vyhledávání sekvencí.

    Tato funkce pomocí podprocesu spustí vytvořený ukázkový příklad pro demonstraci funkcionality nástroje
    pro vyhledávání sekvencí.

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

    tool_path = ospath.join("es_tools", "tools", "sequence_search_tool", "sequence_search_tool.py")
    data_path = ospath.join("es_tools", "examples", "sequence_search_tool", "data")

    match example_number:
        case 1:
            # python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py
            #     -i es_tools/examples/sequence_search_tool/data/1_dna_single_5_3_accepted.txt -s TCAGA -t 53
            command = command + tool_path + " -i " + ospath.join(data_path, "1_dna_single_5_3_accepted.txt") + \
                      " -s TCAGA -t 53"
        case 1:
            # python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py
            #     -i es_tools/examples/sequence_search_tool/data/2_dna_single_3_5_reversed_accepted.txt
            #     -s TCACCATC -t 35_reversed
            command = command + tool_path + " -i " + ospath.join(data_path, "2_dna_single_3_5_reversed_accepted.txt") + \
                      " -s TCACCATC -t 35_reversed"
        case 1:
            # python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py
            #     -i es_tools/examples/sequence_search_tool/data/3_dna_single_3_5_rejected.txt -s ATCTCGGGAGGCG -t 35
            command = command + tool_path + " -i " + ospath.join(data_path, "3_dna_single_3_5_rejected.txt") + \
                      " -s ATCTCGGGAGGCG -t 35"
        case 1:
            # python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py
            #     -i es_tools/examples/sequence_search_tool/data/4_dna_both_accepted.txt -s GTCAAA GAGGC -t both
            command = command + tool_path + " -i " + ospath.join(data_path, "4_dna_both_accepted.txt") + \
                      " -s GTCAAA GAGGC -t both"
        case 1:
            # python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py
            #     -i es_tools/examples/sequence_search_tool/data/5_rna_search_single_accepted.txt -s CGAUUGGGA
            command = command + tool_path + " -i " + ospath.join(data_path, "5_rna_search_single_accepted.txt") + \
                      " -s CGAUUGGGA"
        case 1:
            # python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py
            #     -i es_tools/examples/sequence_search_tool/data/6_rna_search_single_rejected.txt -s CGAUUAA
            command = command + tool_path + " -i " + ospath.join(data_path, "6_rna_search_single_rejected.txt") + \
                      " -s CGAUUAA"
        case 1:
            # python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py
            #     -i es_tools/examples/sequence_search_tool/data/7_rna_search_multiple_accepted.txt -s GUCA CCC UUU
            command = command + tool_path + " -i " + ospath.join(data_path, "7_rna_search_multiple_accepted.txt") + \
                      " -s GUCA CCC UUU"
        case 1:
            # python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py
            #     -i es_tools/examples/sequence_search_tool/data/8_rna_search_multiple_rejected.txt -s GUCA CCC AAA
            command = command + tool_path + " -i " + ospath.join(data_path, "8_rna_search_multiple_rejected.txt") + \
                      " -s GUCA CCC AAA"
        case 1:
            # python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py
            #     -i es_tools/examples/sequence_search_tool/data/9_rna_secondary_structure_accepted.txt
            #     -s "[[[:)):" "(((:"
            command = command + tool_path + " -i " + \
                      ospath.join(data_path, "9_rna_secondary_structure_accepted.txt") + \
                      " -s \"[[[:)):\" \"(((:\""
        case 1:
            # python3 es_tools/tools/sequence_search_tool/sequence_search_tool.py
            #     -i es_tools/examples/sequence_search_tool/data/10_rna_secondary_structure_rejected.txt
            #     -s "::::::::::::" ":[[:[["
            command = command + tool_path + " -i " + \
                      ospath.join(data_path, "10_rna_secondary_structure_rejected.txt") + \
                      " -s \"::::::::::::\" \":[[:[[\""
        case other:
            command = ""

    try:
        run_tool(no_install_run, command, verbose, greedy_quantifier)
    except InvalidExampleNumberException:
        raise
