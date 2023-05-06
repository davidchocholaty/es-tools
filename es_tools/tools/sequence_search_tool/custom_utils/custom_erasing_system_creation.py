"""Vytvoření vymazávacího systému aplikovaného na vyhledávání sekvencí.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci pro vytvoření vymazávacího systému aplikovaného na vyhledávání sekvencí.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: custom_erasing_system_creation.py
"""

from es_tools.formal_models.erasing_system.erasing_system import ErasingSystem
from es_tools.shared_utils.shared_constants import SUBSEQUENCE_LABEL


def create_custom_erasing_system(subsequences: list[str], greedy_quantifier: bool, verbose: bool) -> ErasingSystem:
    """Vytvoření vymazávacího systému pro vyhledávání podsekvencí ve vstupní sekvenci.

    :param subsequences: vyhledávané podsekvence ve vstupní sekvenci.
    :param greedy_quantifier: typ kvantifikátoru (True — chamtivý, False — líný).
    :type greedy_quantifier: bool
    :param verbose: určení, zda mají být vypisovány na standardní výstup při činnosti vymazávacího systému podrobné
                    informace.
    :type verbose: bool
    :return: vytvořený vymazávací systém dle zadaných parametrů.
    :rtype: ErasingSystem
    :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci.
    :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního výrazu
                                                    pro regulární jazyk.
    """
    erasing_strings = set()

    regular_language = ""

    for search_subsequence in subsequences:
        erasing_strings.add(SUBSEQUENCE_LABEL + search_subsequence)
        regular_language = regular_language + "(" + SUBSEQUENCE_LABEL + search_subsequence + ")+"

    return ErasingSystem(erasing_strings, regular_language, False, greedy_quantifier, verbose)
