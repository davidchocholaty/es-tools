"""Nástroje pro porovnání řetězců s regulárním jazykem a výpočtu úrovní shody.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje nástroje pro porovnávání řetězců s regulárním jazykem. Významnou implementovanou funkcí je funkce
match_transformed_language() která provádí kontrolu řetězce s upraveným regulárním jazykem, aby bylo možné ověřovat
i částečné shody řetězce. Dále soubor obsahuje funkci calculate_levels() pro výpočet úrovní shody. Ta kalkuluje úroveň
posledního podvýrazu shody řetězce s regulárním výrazem pro regulární jazyk a také úrovně počtů opakování prvků
jednotlivých podvýrazů regulárního výrazu v řetězci.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: match_language_tools.py
"""

import re

from typing import Any, AnyStr, List, Tuple

from es_tools.formal_models.erasing_system.custom_utils.convert_parentheses_expression_to_extension_string \
    import convert_parentheses_expression_to_extension_string
from es_tools.formal_models.erasing_system.custom_utils.custom_constants import DEFAULT_MATCH_LEVEL
from es_tools.formal_models.erasing_system.custom_utils.parentheses_expression_contains_string \
    import parentheses_expression_contains_string


def calculate_levels(match_groups: Tuple[AnyStr | Any, ...], compared_language: List[str],
                     input_string: str) -> Tuple[int, List[int]]:
    """Výpočet úrovně shody a úrovní počtu opakování podvýrazů pro regulární výraz a vstupní řetězec.

    Tato funkce slouží pro výpočet úrovní shody. Jedná se konkrétně o dva typy úrovní. První určuje úroveň posledního
    podvýrazu shody řetězce s regulárním výrazem pro regulární jazyk. Druhý typ je seznamem a určuje úrovně počtu
    opakování prvků jednotlivých podvýrazů regulárního výrazu ve vstupním řetězci.

    :param match_groups: skupiny shody podvýrazů regulárního výrazů pro regulární jazyk se vstupním řetězcem.
    :type match_groups: Tuple[AnyStr | Any, ...]
    :param compared_language: porovnávaný regulární jazyk (regulární výraz pro regulární jazyk).
    :type compared_language: List[str]
    :param input_string: vstupní řetězec.
    :type input_string: str
    :return: dvojice obsahující vypočítané úrovně. První prvek dvojice představuje úrověň posledního podvýrazu shody
             řetězce s regulárním výrazem pro regulární jazyk. Druhý prvek, který je seznamem, obsahuje úrovně počtů
             opakování prvků jednotlivých podvýrazů regulárního výrazu v řetězci.
    :rtype: Tuple[int, List[int]]
    """
    match_level = len([element for element in compared_language if element not in ["*", "+"]])
    quantifiers_levels = list()

    for i in range(len(match_groups)):
        group = match_groups[i]
        repeats_number = 0

        if group is not None:
            while input_string.startswith(group):
                repeats_number = repeats_number + 1
                input_string = input_string[len(group):]

        quantifiers_levels.append(repeats_number)

    return match_level, quantifiers_levels


def match_extended_language_ending_with_operator(compared_language: List[str],
                                                 input_string: str) -> Tuple[bool, int, List[int]]:
    """Funkce pro úpravu porovnávaného regulárního jazyka končícího operátorem s řetězcem.

    Tato funkce slouží pro úpravu regulárního jazyka končícího operátorem „*“ nebo „+“, kterému předchází podvýraz
    v klasických závorkách. Konkrétně dochází k patřičnému rozšíření posledního podvýrazu tak, aby kromě řetězců
    obsažených v posledním podvýrazu byly porovnávány i všechny podřetězce těchto řetězců. Tím je docíleno, že může
    docházet i k pouze částečné shodě řetězce s regulárním výrazem. Konkrétní rozšíření porovnávaného regulárního
    výrazu provádí volaná funkce convert_parentheses_expression_to_extension_string().

    :param compared_language: porovnávaný regulární výraz pro regulární jazyk.
    :type compared_language: List[str]
    :param input_string: vstupní řetězec.
    :type input_string: str
    :return: výsledek porovnání, přičemž jednotlivé prvky trojice představují po řadě: 1. zda řetězec může náležet
             do porovnávaného regulárního jazyka, přičemž poslední podvýraz regulárního výrazu pro porovnávaný
             regulární jazyk nemusí být zcela obsažen ve vstupním řetězci a pro tento podvýraz může docházet pouze
             k částečné shodě, 2. úroveň posledního podvýrazu shody vstupního řetězce s regulárním výrazem pro
             regulární jazyk, 3. úrovně počtů opakování jednotlivých prvků podvýrazů regulárního výrazu ve vstupním
             řetězci.
    :rtype: Tuple[bool, int, List[int]]
    """
    match = False
    match_level = DEFAULT_MATCH_LEVEL
    quantifiers_levels = list()

    last_but_one_compared_language_element = compared_language[-2]
    last_compared_language_element = compared_language[-1]

    # Následující podmínka ověřuje situaci, že poslední podvýraz regulárního výrazu obsahuje řetězec delší jak dva
    # symboly. V takovém případě je zapotřebí provést rozšíření porovnávaného regulárního výrazu. Pokud ne, dle návrhu
    # algoritmu daná funkce by nebyla volána, pokud by řetězec náležel do regulárního jazyka bez modifikace, a tudíž
    # vstupní řetězec nenáleží do regulárního jazyka a není zapotřebí provádět porovnání.
    if parentheses_expression_contains_string(last_but_one_compared_language_element):
        extended_compared_regular_language = compared_language.copy()

        # Pokud byl posledním operátorem symbol „+“, musí být změněn na symbol „*“, tudíž rozšíření porovnávaného
        # jazyka má význam. Například regulární výraz končící podčástí (a|bcd)+ bude rozšířen o výraz (b|bc)
        # a vznikne nový konec regulárního výrazu: (a|bcd)*(b|bc).
        if last_compared_language_element == "+":
            extended_compared_regular_language[-1] = "*"

        extended_compared_regular_language.append(
            convert_parentheses_expression_to_extension_string(
                last_but_one_compared_language_element))

        match_result = re.fullmatch("".join(extended_compared_regular_language), input_string)

        if match_result:
            match = True
            match_level, quantifiers_levels = calculate_levels(match_result.groups(),
                                                               compared_language,
                                                               input_string)

    return match, match_level, quantifiers_levels


def match_transformed_language_parentheses(compared_language: List[str],
                                           input_string: str) -> Tuple[bool, int, List[int]]:
    """Funkce pro úpravu porovnávaného regulárního jazyka končícího podvýrazem v klasických závorkách.

    Tato funkce slouží pro úpravu regulárního jazyka končícího podvýrazem v klasických závorkách. Konkrétně dochází
    k patřičné modifikaci posledního podvýrazu regulárního výrazu tak, aby kromě řetězců obsažených v posledním
    podvýrazu byly porovnávány i všechny podřetězce těchto řetězců. Tím je docíleno, že může docházet i k pouze
    částečné shodě řetězce s regulárním výrazem. Získání nového nahrazujícího výrazu pro poslední podvýraz poskytuje
    volaná funkce convert_parentheses_expression_to_extension_string().

    :param compared_language: porovnávaný regulární výraz pro regulární jazyk.
    :type compared_language: List[str]
    :param input_string: vstupní řetězec.
    :type input_string: str
    :return: výsledek porovnání, přičemž jednotlivé prvky trojice představují po řadě: 1. zda řetězec může náležet
             do porovnávaného regulárního jazyka, přičemž poslední podvýraz regulárního výrazu pro porovnávaný
             regulární jazyk nemusí být zcela obsažen ve vstupním řetězci a pro tento podvýraz může docházet pouze
             k částečné shodě, 2. úroveň posledního podvýrazu shody vstupního řetězce s regulárním výrazem pro
             regulární jazyk, 3. úrovně počtů opakování jednotlivých prvků podvýrazů regulárního výrazu ve vstupním
             řetězci.
    :rtype: Tuple[bool, int, List[int]]
    """
    match = False
    match_level = DEFAULT_MATCH_LEVEL
    quantifiers_levels = list()

    last_compared_language_element = compared_language[-1]

    # Pokud je posledním prvkem regulárního výrazu podvýraz v klasických závorkách, je zapotřebí zkontrolovat,
    # zda neobsahuje řetězec se dvěma nebo více symboly, takže porovnávaný jazyk je zapotřebí upravit.
    if parentheses_expression_contains_string(last_compared_language_element):
        extended_compared_regular_language = compared_language.copy()

        # Protože vstupní řetězec nenáležel celému porovnávanému regulárnímu výrazu, bude poslední podvýraz v závorkách
        # transformován na výraz, který obsahuje všechny podřetězce uvedených řetězců vyjma vlastních podřetězců
        # (podřetězců shodných s původním řetězcem). Poslední podvýraz bude nahrazen rozšiřujícím výrazem.
        extended_compared_regular_language[-1] = \
            convert_parentheses_expression_to_extension_string(last_compared_language_element)

        match_result = re.fullmatch("".join(extended_compared_regular_language), input_string)

        if match_result:
            match = True
            match_level, quantifiers_levels = calculate_levels(match_result.groups(),
                                                               compared_language,
                                                               input_string)

    return match, match_level, quantifiers_levels


def match_transformed_language_operator(compared_language: List[str],
                                        input_string: str) -> Tuple[bool, int, List[int]]:
    """Pomocná funkce pro porovnání řetězce s upraveným regulárním výrazem končícím operátorem.

    Tato funkce slouží jako pomocná funkce pro případ, kdy regulární výraz má být upraven, pričemž končí jedním
    z operátorů: „*“ nebo „+“. Hlavní úlohou funkce je ověření, že před zmíněným operátorem se nachází výraz
    v klasických závorkách. Samotnou modifikaci porovnávaného regulárního výrazu ponechává na volané funkci
    match_extended_language_ending_with_operator().

    :param compared_language: porovnávaný regulární výraz pro regulární jazyk.
    :type compared_language: List[str]
    :param input_string: vstupní řetězec.
    :type input_string: str
    :return: výsledek porovnání, přičemž jednotlivé prvky trojice představují po řadě: 1. zda řetězec může náležet
             do porovnávaného regulárního jazyka, přičemž poslední podvýraz regulárního výrazu pro porovnávaný
             regulární jazyk nemusí být zcela obsažen ve vstupním řetězci a pro tento podvýraz může docházet pouze
             k částečné shodě, 2. úroveň posledního podvýrazu shody vstupního řetězce s regulárním výrazem pro
             regulární jazyk, 3. úrovně počtů opakování jednotlivých prvků podvýrazů regulárního výrazu ve vstupním
             řetězci.
    :rtype: Tuple[bool, int, List[int]]
    """
    last_but_one_compared_language_element = compared_language[-2]

    # Kontrola, zda předposledním prvkem porovnávaného jazyka je výraz v klasických závorkách.
    if re.fullmatch(r"\(.+?\)", last_but_one_compared_language_element):
        return match_extended_language_ending_with_operator(compared_language, input_string)

    return False, DEFAULT_MATCH_LEVEL, list()


def match_transformed_language(compared_language: List[str], input_string: str) -> Tuple[bool, int, List[int]]:
    """Porovnání řetězce s upraveným regulárním výrazem pro regulární jazyk.

    Tato funkce poskytuje porovnání vstupního řetězce s regulárním výrazem pro regulární jazyk. Daný regulární výraz
    ovšem podléhá jistým úpravám. Konkrétně mohou nastat dva případy. V prvním případě může regulární výraz končit
    operátorem „*“ nebo „+“, kterému předchází výraz v klasických závorkách. Pro takový regulární jazyk je zapotřebí
    upravit regulární výraz tak, že budou porovnávány i všechny podřetězce řetězců obsažených v posledním podvýrazu
    v závorkách. Na základě tohoto porovnání je možné určit, zda řetězec může i pouze částečně náležet do porovnávaného
    regulárního jazyka. V druhém případě regulární výraz končí pouze podvýrazem v závorkách. Modifikace regulárního
    výrazu se velmi podobá uvedenému postupu, ovšem obsahuje jisté odlišnosti na základě skutečnosti, že regulární
    výraz nekončí jedním z dříve zmíněných operátorů.

    :param compared_language: porovnávaný regulární výraz pro regulární jazyk.
    :type compared_language: List[str]
    :param input_string: vstupní řetězec.
    :type input_string: str
    :return: výsledek porovnání, přičemž jednotlivé prvky trojice představují po řadě: 1. zda řetězec může náležet
             do porovnávaného regulárního jazyka, přičemž poslední podvýraz regulárního výrazu pro porovnávaný
             regulární jazyk nemusí být zcela obsažen ve vstupním řetězci a pro tento podvýraz může docházet pouze
             k částečné shodě, 2. úroveň posledního podvýrazu shody vstupního řetězce s regulárním výrazem pro
             regulární jazyk, 3. úrovně počtů opakování jednotlivých prvků podvýrazů regulárního výrazu ve vstupním
             řetězci.
    :rtype: Tuple[bool, int, List[int]]
    """
    match = False
    match_level = DEFAULT_MATCH_LEVEL
    quantifiers_levels = list()

    last_compared_language_element = compared_language[-1]

    # Kontrola, zda je posledním prvkem porovnávaného jazyka operátor "*" nebo "+".
    if last_compared_language_element in ["*", "+"]:
        # Pokud ano, může být nutné rozšířit předchozí výraz v závorkách tak, aby také byly porovnávány jednotlivé
        # podřetězce požadovaných řetězců.
        match, match_level, quantifiers_levels = match_transformed_language_operator(compared_language,
                                                                                     input_string)

    elif re.fullmatch(r"\(.+?\)", last_compared_language_element):
        match, match_level, quantifiers_levels = match_transformed_language_parentheses(compared_language,
                                                                                        input_string)

    return match, match_level, quantifiers_levels
