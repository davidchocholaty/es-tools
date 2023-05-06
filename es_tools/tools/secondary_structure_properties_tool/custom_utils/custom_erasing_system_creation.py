"""Vytvoření vymazávacího systému aplikovaného na ověření vlastností sekundární struktury RNA pro minimum nebo maximum.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci pro vytvoření vymazávacího systému aplikovaného na ověření vlastností sekundární
struktury RNA pro minimum nebo maximum.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: custom_erasing_system_creation.py
"""

from es_tools.formal_models.erasing_system.erasing_system import ErasingSystem
from es_tools.tools.secondary_structure_properties_tool.custom_utils.custom_constants import PAIRED_SYMBOL,\
    UNPAIRED_SYMBOL


def create_erasing_system(min_max_flag: bool, greedy_quantifier: bool, verbose: bool) -> ErasingSystem:
    """Vytvoření vymazávacího systému pro ověření vlastností sekundární struktury RNA pro minimum nebo maximum.

    :param min_max_flag: určení, zda vymazávací systém má ověřovat vlastnosti pro minimální nebo maximální hodnotu.
                         Na základě tohoto parametru je určen regulární jazyk vymazávacího systému.
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
    erasing_strings = {PAIRED_SYMBOL, UNPAIRED_SYMBOL}

    regular_language = "(" + UNPAIRED_SYMBOL + PAIRED_SYMBOL + ")*"

    if min_max_flag:
        regular_language = regular_language + PAIRED_SYMBOL + "*"
    else:
        regular_language = regular_language + UNPAIRED_SYMBOL + "*"

    return ErasingSystem(erasing_strings, regular_language, False, greedy_quantifier, verbose)
