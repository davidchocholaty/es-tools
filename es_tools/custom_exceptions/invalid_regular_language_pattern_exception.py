"""Výjimka pro zadání neplatného regulárního jazyka nebo použití nepovolených vzorů v regulárním výrazu.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že zadaný regulární výraz není dle stanovených pravidel platný.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: invalid_regular_language_exception.py
"""


class InvalidRegularLanguagePatternException(Exception):
    """Výjimka pro zadání neplatného regulárního jazyka nebo použití nepovolených vzorů v regulárním výrazu.

    Tato třída reprezentuje zadání nevalidního regulárního jazyka vůči stanoveným pravidlům. Jako výjimka je odvozena
    od třídy Exception.
    """
    def __init__(self, msg="Invalid regular language definition pattern.") -> None:
        """**Konstruktor třídy InvalidRegularLanguagePatternException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
