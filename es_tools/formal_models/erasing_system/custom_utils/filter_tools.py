"""Nástroje pro vymazávací systém na bázi filtrování.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje pomocné funkce pro algoritmus činnosti vymazávacího systému, přičemž jejich funkcionalita je
založena především na bázi filtrování. Konkrétně se jedná o funkci filter_quantifier_levels(), která vybere úrovně
shody řetězce s regulárním jazykem dle příslušných požadavků, a o funkci filter_applicable_erasing_strings(), která
na základě parametrů vybere odpovídající aplikovatelné vymazávací řetězce.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: filter_tools.py
"""

from sys import maxsize
from typing import List, Tuple

from es_tools.formal_models.erasing_system.custom_utils.custom_constants import MATCH_LEVEL_TUPLE_INDEX, \
    QUANTIFIERS_LEVELS_TUPLE_INDEX


def filter_quantifier_levels(applicable_erasing_strings: List[Tuple[str, int, List[int]]],
                             chosen_match_level: int,
                             quantifier_type_greedy: bool) -> List[List[int]]:
    """Výběr úrovní počtu opakování podvýrazů při shodě řetězce s regulárním jazykem.

    Tato funkce nejprve vybírá aplikovatelné vymazávací řetězce na základě úrovně shody řetězce s regulárním jazykem,
    přičemž jako úroveň se uvažuje poslední podvýraz shody. Dále na základě jednotlivých podvýrazů regulárního výrazu
    pro regulární jazyk funkce provádí druhou filtraci, a to na základě opakování jednotlivých prvků podvýrazů
    v příslušném vymazávacím řetězci. Konečný seznam poté funkce navrací jako výsledek výběru.

    :param applicable_erasing_strings: seznam aplikovatelných vymazávacích řetězců.
    :type applicable_erasing_strings: List[Tuple[str, int, List[int]]]
    :param chosen_match_level: vybraná úroveň shody řetězce s regulárním jazykem - úroveň posledního podvýrazu shody.
    :type chosen_match_level: int
    :param quantifier_type_greedy: typ kvantifikátoru (True — chamtivý, False — líný).
    :type quantifier_type_greedy: bool
    :return: seznam seznamů vybraných úrovní shody.
    :rtype: List[List[int]]
    """
    chosen_quantifiers_levels = list()

    # První filtrace na základě úrovně posledního podvýrazu shody.
    for erasing_string_tuple in applicable_erasing_strings:
        if erasing_string_tuple[MATCH_LEVEL_TUPLE_INDEX] == chosen_match_level:
            chosen_quantifiers_levels.append(erasing_string_tuple[QUANTIFIERS_LEVELS_TUPLE_INDEX])

    if quantifier_type_greedy:
        min_max_function = max
    else:
        min_max_function = min

    # Druhá filtrace na základě počtu opakování prvků jednotlivých podvýrazů.
    i = 0
    while i < chosen_match_level and len(chosen_quantifiers_levels) > 1:
        if quantifier_type_greedy:
            repeats = 0
        else:
            repeats = maxsize

        for repeats_list in chosen_quantifiers_levels:
            if len(repeats_list) > i:
                repeats = min_max_function(repeats, repeats_list[i])

        number_of_quantifiers_lists = len(chosen_quantifiers_levels)

        for j in range(number_of_quantifiers_lists - 1, -1, -1):
            if len(chosen_quantifiers_levels[j]) > i:
                if chosen_quantifiers_levels[j][i] != repeats:
                    del chosen_quantifiers_levels[j]

        i = i + 1

    return chosen_quantifiers_levels


def filter_applicable_erasing_strings(applicable_erasing_strings: List[Tuple[str, int, List[int]]],
                                      chosen_quantifiers_levels: List[List[int]],
                                      chosen_match_level: int) -> List[Tuple[str, int, List[int]]]:
    """Výběr aplikovatelých vymazávacích řetězců na základě úrovně shody a počtu opakování podvýrazů.

    Tato funkce provádí výběr aplikovatelných vymazávacích řetězců. Konkrétně je výběr proveden na základě dvou
    kritérií. Prvním kritériem je úroveň posledního podvýrazu shody řetězce s regulárním jazykem, přičemž jako řetězec
    je uvažován řetězec vzniklý konkatenací všech použitých vymazávacích řetězců a ověřovaného následujícího
    vymazávacího řetězce. Druhým kritériem jsou jednotlivé počty opakování prvků podvýrazu regulárního výrazu
    pro regulární jazyk ve zmíněném řetězci. Na základě parametrů jsou dle popsaných postupů vybrány aplikovatelné
    vymazávací řetězce splňující veškeré požadavky.

    :param applicable_erasing_strings: aplikovatelné vymazávací řetězce.
    :type applicable_erasing_strings: List[Tuple[str, int, List[int]]]
    :param chosen_quantifiers_levels: vybrané úrovně počtů opakování podvýrazů regulárního výrazu pro regulární jazyk.
    :type chosen_quantifiers_levels: List[List[int]]
    :param chosen_match_level: vybraná úroveň posledního podvýrazu shody.
    :type chosen_match_level: int
    :return: výsledek výběru aplikovatelných vymazávacích řetězců, které splňují požadavky definované hodnotami
             parametrů.
    :rtype: List[Tuple[str, int, List[int]]]
    """
    filtered_applicable_erasing_strings = list()

    for erasing_string_tuple in applicable_erasing_strings:
        if erasing_string_tuple[MATCH_LEVEL_TUPLE_INDEX] == chosen_match_level and \
                erasing_string_tuple[QUANTIFIERS_LEVELS_TUPLE_INDEX] in chosen_quantifiers_levels:
            filtered_applicable_erasing_strings.append(erasing_string_tuple)

    return filtered_applicable_erasing_strings
