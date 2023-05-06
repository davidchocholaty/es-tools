"""Vytvoření vymazávacího systému aplikovaného na ověření správnosti řešení problému n dam v diagonálních souřadnicích.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci pro vytvoření vymazávacího systému aplikovaného na ověření správnosti řešení problému
n dam v diagonálních souřadnicích.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: custom_erasing_system_diagonal_coordinates_creation.py
"""


from es_tools.formal_models.erasing_system.erasing_system import ErasingSystem
from es_tools.shared_utils.greek_alphabet import greek_alphabet
from es_tools.tools.n_queens_problem_tool.custom_utils.english_alphabet import english_alphabet


def create_erasing_system_diagonal_coordinates(board_size: int, greedy_quantifier: bool, verbose: bool) -> ErasingSystem:
    """Vytvoření vymazávacího systému pro ověření vstupního řešení problému n dam v diagonálních souřadnicích.

    :param board_size: rozměr šachovnice pro vstupní řešení.
    :type board_size: int
    :param greedy_quantifier: typ kvantifikátoru (True — chamtivý, False — líný).
    :type greedy_quantifier: bool
    :param verbose: určení, zda mají být vypisovány na standardní výstup při činnosti vymazávacího systému podrobné
                    informace.
    :type verbose: bool
    :return: vytvořený vymazávací systém dle zadaného rozměru šachovnice.
    :rtype: ErasingSystem
    :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci.
    :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního výrazu
                                                    pro regulární jazyk.
    """
    erasing_strings_diagonal = set(greek_alphabet[0:2 * board_size - 1]).union(set(english_alphabet[0:2 * board_size - 1]))
    regular_language_symbols = "".join(greek_alphabet[0:2 * board_size - 1]) + "".join(
        english_alphabet[0:2 * board_size - 1])

    regular_language_diagonal = "("

    for symbol in regular_language_symbols:
        regular_language_diagonal = regular_language_diagonal + symbol + symbol + "|"

    regular_language_diagonal = regular_language_diagonal[:-1] + ")" + "("

    for symbol in regular_language_symbols:
        regular_language_diagonal = regular_language_diagonal + symbol + "|"

    regular_language_diagonal = regular_language_diagonal[:-1] + ")*"

    return ErasingSystem(erasing_strings_diagonal, regular_language_diagonal, False, greedy_quantifier, verbose)
