"""Výjimka pro zadání nesprávného čísla ukázkového příkladu.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že zadané číslo ukázkového příkladu není v příslušném rozsahu.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: invalid_example_number_exception.py
"""


class InvalidExampleNumberException(Exception):
    """Výjimka pro zadání nesprávného čísla ukázkového příkladu.

    Tato třída reprezentuje zadání čísla ukázkového příkladu mimo příslušný rozsah. Jako výjimka je odvozena
    od třídy Exception.
    """
    def __init__(self, msg="An invalid example number was entered.") -> None:
        """**Konstruktor třídy InvalidExampleNumberException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
