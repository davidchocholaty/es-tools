"""Vytvoření vymazávacího systému aplikovaného na ověření vyvážených závorek.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci pro vytvoření vymazávacího systému aplikovaného na ověření vyvážených závorek.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: custom_erasing_system_creation.py
"""

from es_tools.formal_models.erasing_system.erasing_system import ErasingSystem


def create_erasing_system(greedy_quantifier: bool, verbose: bool) -> ErasingSystem:
    """Vytvoření vymazávacího systému pro ověření vyvážených závorek.

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
    erasing_strings = {"Aa", "Bb", "Cc"}
    regular_language = "(Aa|Bb|Cc)*"

    return ErasingSystem(erasing_strings, regular_language, False, greedy_quantifier, verbose)
