"""Ověření, zda výraz v závorkách obsahuje řetězec s délkou větší než jeden symbol.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: parentheses_expression_contains_string.py
"""


def parentheses_expression_contains_string(expression: str) -> bool:
    """Ověření, zda výraz v závorkách obsahuje řetězec s délkou větší než jeden symbol.

    Tato funkce slouží pro ověření, zda výraz v závorkách obsahuje řetězec s délkou větší než jeden symbol. Jak již
    název funkce napovídá, je předpokládáno, že vstupní výraz je výrazem v klasických závorkách. Samotný první
    a poslední symbol výrazu není kontrolován na základě skutečnosti, že dle návrhu algoritmu již daná kontrola
    byla provedena.

    :param expression: vstupní výraz.
    :type expression: str
    :return: True, pokud výraz v závorkách obsahuje řetězec s délkou větší než jeden symbol, jinak False.
    :rtype: bool
    """
    strings = expression[1:-1].split("|")

    for string_element in strings:
        if len(string_element) > 1:
            return True

    return False
