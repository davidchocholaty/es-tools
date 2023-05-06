"""Převod výrazu v závorkách na řetězec pro modifikaci regulárního výrazu.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci convert_parentheses_expression_to_extension_string() pro převod výrazu v závorkách
na řetězec pro modifikaci regulárního výrazu. Daný převedený výraz jednotlivé funkce využívající tak, že buď je
regulární výraz rozšířen o nový výraz nebo je poslední podvýraz nahrazen novým výrazem. Typ modifikace se odvíjí
od skutečnosti, zda regulární výraz končí výrazem v závorkách nebo jedním z operátorů „*“ nebo „+“.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: convert_parentheses_expression_to_extension_string.py
"""

from re import sub


def convert_parentheses_expression_to_extension_string(expression_to_convert: str) -> str:
    """Funkce pro převod výrazu v závorkách na řetězec pro modifikaci regulárního výrazu.

    Tato funkce slouží pro převod vstupního výrazu na výraz pro úpravu regulárního výrazu. Konkrétně nový výraz
    modifikuje vstupní výraz tak, že kromě obsažených řetězců, jenž obsahují více jak jeden symbol, jsou přidány
    i veškeré jejich podřetězce. Například výraz „(a|bcd)“ bude upraven na výraz „(b|bc)“. Jak již název funkce
    napovídá, je předpokládáno, že vstupní výraz je výrazem v klasických závorkách. Samotný první a poslední symbol
    výrazu není kontrolován na základě skutečnosti, že dle návrhu algoritmu již daná kontrola byla provedena.

    :param expression_to_convert: vstupní výraz pro převod na nový výraz.
    :type expression_to_convert: str
    :return: nový rozšiřující výraz vstupního výrazu.
    :rtype: str
    """
    extension_string = "("
    to_process = expression_to_convert[1:-1].split("|")

    for string_element in to_process:
        for substring_end_index in range(1, len(string_element)):
            extension_string = extension_string + string_element[0:substring_end_index] + "|"

    if len(extension_string) == 1:
        return ""

    return sub(r".$", ")", extension_string)
