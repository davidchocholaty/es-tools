"""Skript pro spuštení ukázkového příkladu pro demonstraci funkcionality nástroje pro vyhledávání proteinů a sekvencí
aminokyselin proteinů.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje implementaci pomocného nástroje pro spuštění jednotlivých ukázkových příkladů implementovaného
nástroje reprezentujícího aplikaci vymazávacího systému pro vyhledávání proteinů a sekvencí aminokyselin proteinů.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: run_example_amino_acid_sequence_search_tool.py
"""

from os import path as ospath

from es_tools.custom_exceptions.invalid_example_number_exception import InvalidExampleNumberException
from es_tools.custom_exceptions.unknown_platform_system_exception import UnknownPlatformSystemException
from es_tools.examples.custom_utils.run_tool import run_tool
from es_tools.examples.custom_utils.set_python_command_os_type import set_python_command_os_type


def run_example_amino_acid_sequence_search_tool(no_install_run: bool,
                                                example_number: int,
                                                verbose: bool,
                                                greedy_quantifier: bool) -> None:
    """Spuštění příkladu pro prezentaci ukázkového příkladu nástroje pro vyhledávání proteinů a sekvencí aminokyselin
    proteinů.

    Tato funkce pomocí podprocesu spustí vytvořený ukázkový příklad pro demonstraci funkcionality nástroje
    pro vyhledávání proteinů a sekvencí aminokyselin proteinů.

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

    tool_path = ospath.join("es_tools", "tools", "amino_acid_sequence_search_tool", "amino_acid_sequence_search_tool.py")
    data_path = ospath.join("es_tools", "examples", "amino_acid_sequence_search_tool", "data")

    match example_number:
        case 1:
            # python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py
            #     -i es_tools/examples/amino_acid_sequence_search_tool/data/1_protein_accepted.txt -s MALGHR -n
            command = command + tool_path + " -i " + ospath.join(data_path, "1_protein_accepted.txt") + " -s MALGHR -n"
        case 2:
            # python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py
            #     -i es_tools/examples/amino_acid_sequence_search_tool/data/2_protein_rejected.txt -s MALGHRG -n
            command = command + tool_path + " -i " + ospath.join(data_path, "2_protein_rejected.txt") + " -s MALGHRG -n"
        case 3:
            # python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py
            #     -i es_tools/examples/amino_acid_sequence_search_tool/data/3_amino_acid_sequence_accepted.txt
            #     -b TSKSLWE -n
            command = command + tool_path + " -i " + ospath.join(data_path, "3_amino_acid_sequence_accepted.txt") + \
                      " -b TSKSLWE -n"
        case 4:
            # python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py
            #     -i es_tools/examples/amino_acid_sequence_search_tool/data/4_amino_acid_sequence_rejected.txt
            #     -b DVDVT -n
            command = command + tool_path + " -i " + ospath.join(data_path, "4_amino_acid_sequence_rejected.txt") + \
                      " -b DVDVT -n"
        case 5:
            # python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py
            #     -i es_tools/examples/amino_acid_sequence_search_tool/data/5_both_accepted.txt -s MALGHR -b DVDVLRET -n
            command = command + tool_path + " -i " + ospath.join(data_path, "5_both_accepted.txt") + \
                      " -s MALGHR -b DVDVLRET -n"
        case 6:
            # python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py
            #     -i es_tools/examples/amino_acid_sequence_search_tool/data/6_both_protein_rejected.txt
            #     -s MALGHRG -b DVDVLRET -n
            command = command + tool_path + " -i " + ospath.join(data_path, "6_both_protein_rejected.txt") + \
                      " -s MALGHRG -b DVDVLRET -n"
        case 7:
            # python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py
            #     -i es_tools/examples/amino_acid_sequence_search_tool/data/7_both_multiple_accepted.txt
            #     -s MALGHR MSFGRLTSKSLWETDVDVLRETDKGEESPGFIEQGAR  -b MAT QAEQN -n
            command = command + tool_path + " -i " + ospath.join(data_path, "7_both_multiple_accepted.txt") + \
                      " -s MALGHR MSFGRLTSKSLWETDVDVLRETDKGEESPGFIEQGAR  -b MAT QAEQN -n"
        case 8:
            # python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py
            #     -i es_tools/examples/amino_acid_sequence_search_tool/data/8_both_multiple_rejected_overlapped.txt
            #     -s MALGHR MSFGRLTSKSLWETDVDVLRETDKGEESPGFIEQGAR  -b MATAAQA QAEQN -n
            command = command + tool_path + " -i " + \
                      ospath.join(data_path, "8_both_multiple_rejected_overlapped.txt") + \
                      " -s MALGHR MSFGRLTSKSLWETDVDVLRETDKGEESPGFIEQGAR  -b MATAAQA QAEQN -n"
        case 9:
            # python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py
            #     -i es_tools/examples/amino_acid_sequence_search_tool/data/9_input_data_rejected_non_terminated.txt
            #     -s MALGHRG -b DVDVLRET
            command = command + tool_path + " -i " + \
                      ospath.join(data_path, "9_input_data_rejected_non_terminated.txt") + \
                      " -s MALGHRG -b DVDVLRET"
        case 10:
            # python3 es_tools/tools/amino_acid_sequence_search_tool/amino_acid_sequence_search_tool.py
            #     -i es_tools/examples/amino_acid_sequence_search_tool/data/10_input_data_without_proteins.txt
            #     -s MALGHRG -b DVDVLRET -n
            command = command + tool_path + " -i " + ospath.join(data_path, "10_input_data_without_proteins.txt") + \
                      " -s MALGHRG -b DVDVLRET -n"
        case other:
            command = ""

    try:
        run_tool(no_install_run, command, verbose, greedy_quantifier)
    except InvalidExampleNumberException:
        raise
