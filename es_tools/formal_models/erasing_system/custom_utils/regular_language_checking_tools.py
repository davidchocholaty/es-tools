"""Nástroje pro ověření tvaru regulárního jazyka.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkce pro kontrolu splnění požadavků na tvar regulárního výrazu pro regulární jazyk.
Fundamentální funkcí je funkce is_valid_regular_language(), která určuje, zda byly požadavky splněny či nikoliv.
Další funkce obsažené v tomto souboru jsou pouze pomocné pro uvedenou funkci.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: regular_language_checking_tools.py
"""

from es_tools.formal_models.erasing_system.custom_utils.not_allowed_regular_language_strings \
    import not_allowed_regular_language_strings


def only_allowed_patterns(regular_language: str) -> bool:
    """Kontrola, zda regulární výraz neobsahuje zakázané symboly či řetězce.

    :param regular_language: regulární výraz pro regulární jazyk.
    :type regular_language: str
    :return: True, pokud regulární výraz neobsahuje nepovolené řetězce, jinak False.
    :rtype: bool
    """
    if any(string in regular_language for string in not_allowed_regular_language_strings):
        return False

    return True


# Následující funkce je založena na kódu, který byl převzat:
# Zdrojový web: Stack Overflow.
# Odkaz na původní otázku: https://stackoverflow.com/questions/72250748/how-to-check-if-the-parentheses-and-brackets-are-balanced
# Autor otázky: MatmataHi (https://stackoverflow.com/users/15589144/matmatahi).
# Otázka upravena: Asclepius (https://stackoverflow.com/users/832230/asclepius).
# Autor odpovědi: Asclepius (https://stackoverflow.com/users/832230/asclepius).
#
# *** Začátek převzatého kódu. ***
def correctly_bracketed_without_nested_brackets(regular_language: str) -> bool:
    """Kontrola správnosti zápisu závorek v regulárním výrazu, přičemž nejsou povoleny jejich vnoření.

    :param regular_language: regulární výraz pro regulární jazyk.
    :type regular_language: str
    :return: True, pokud regulární výraz obsahuje pouze správné uzávorkování a neobsahuje jejich vnoření, jinak False.
    :rtype: bool
    """
    brackets = {"(": ")", "[": "]"}

    stack = []
    for bracket in regular_language:
        if bracket in brackets:  # opening bracket
            if len(stack) > 0:
                stack.clear()
                return False

            stack.append(bracket)
        elif bracket in brackets.values():  # closing bracket
            if (not stack) or (bracket != brackets[stack.pop()]):
                return False

    return not stack
# *** Konec převzatého kódu. ***


def start_with_operator(regular_language: str) -> bool:
    """Kontrola, zda regulární výraz pro regulární jazyk nezačíná symbolem pro operátor.

    :param regular_language: regulární výraz pro regulární jazyk.
    :type regular_language: str
    :return: True, pokud regulární výraz začíná symbolem pro operátor, a tudíž jeho zápis není validní, jinak False.
    :rtype: bool
    """
    if regular_language[0] in ["*", "+", "|"]:
        return True

    return False


def is_valid_regular_language(regular_language: str) -> bool:
    """Ověření validity regulárního výrazu pro regulární jazyk.

    Tato funkce slouží pro ověření validity regulárního výrazu pro regulární jazyk. Především jsou provedeny kontroly,
    zda regulární výraz nezačíná symbolem pro operátor, zda neobsahuje zakázané řetězce a jestli je výraz správně
    uzávorkován, přičemž není povoleno vnoření závorek.

    :param regular_language: regulární výraz pro regulární jazyk.
    :type regular_language: str
    :return: True, pokud regulární výraz je ve validním tvaru a splňuje požadované striktní vlastnosti, jinak False.
    :rtype: bool
    """
    if len(regular_language) == 0:
        return False

    if start_with_operator(regular_language):
        return False

    if not only_allowed_patterns(regular_language):
        return False

    return correctly_bracketed_without_nested_brackets(regular_language)
