"""Výjimka pro zadání nepovoleného symbolu.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že zadaný symbol není povolen.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: illegal_symbol_occurrence_exception.py
"""


class IllegalSymbolOccurrenceException(Exception):
    """Výjimka pro zadání nepovoleného symbolu.

    Tato třída reprezentuje zadání symbolu, který dle striktních pravidel není povolen. Jako výjimka je odvozena
    od třídy Exception.
    """
    def __init__(self, msg="A symbol that is not allowed has been encountered.") -> None:
        """**Konstruktor třídy IllegalSymbolOccurrenceException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
