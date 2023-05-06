"""Vytvoření vymazávacího systému aplikovaného na vyhledávání proteinů a sekvencí aminokyselin proteinů.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci pro vytvoření vymazávacího systému aplikovaného na vyhledávání proteinů a sekvencí
aminokyselin proteinů.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: custom_erasing_system_creation.py
"""

from typing import List

from es_tools.formal_models.erasing_system.erasing_system import ErasingSystem
from es_tools.shared_utils.shared_constants import SUBSEQUENCE_LABEL


def create_custom_erasing_system(sequences: List[str],
                                 subsequences: List[str],
                                 greedy_quantifier: bool,
                                 verbose: bool) -> ErasingSystem:
    """Vytvoření vymazávacího systému pro vyhledávání proteinů a sekvencí aminokyselin proteinů.

    Tato funkce slouží pro vytvoření vymazávacího systému pro vyhledávání proteinů a sekvencí aminokyselin proteinů,
    přičemž jsou jednotlivé vyhledávané sekvence a podsekvence aminokyselin nastaveny dle zadaných parametrů.

    :param sequences: vyhledávané sekvence aminokyselin kódující proteiny.
    :type sequences: List[str]
    :param subsequences: vyhledávané podsekvence aminokyselin proteinů.
    :type subsequences: List[str]
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

    for sequence in sequences:
        sequence_erasing_string = SUBSEQUENCE_LABEL + sequence

        erasing_strings.add(sequence_erasing_string)
        regular_language = regular_language + "(" + sequence_erasing_string + ")+"

    for subsequence in subsequences:
        subsequence_erasing_string = SUBSEQUENCE_LABEL + subsequence

        erasing_strings.add(subsequence_erasing_string)
        regular_language = regular_language + "(" + subsequence_erasing_string + ")+"

    return ErasingSystem(erasing_strings, regular_language, False, greedy_quantifier, verbose)
