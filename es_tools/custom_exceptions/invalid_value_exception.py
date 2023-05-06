"""Výjimka pro zadání neplatné hodnoty vstupního argumentu.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že zadaná hodnota vstupního argumentu není platná.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: invalid_value_exception.py
"""


class InvalidValueException(Exception):
    """Výjimka pro zadání neplatné hodnoty vstupního argumentu.

    Tato třída reprezentuje zadání neplatné hodnoty vstupního argumentu. Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self, msg="The provided value is not valid.") -> None:
        """**Konstruktor třídy InvalidValueException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
