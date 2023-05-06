"""Výjimka pro zadání nesprávného argumentu.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že zadaný vstupní argument neexistuje.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: invalid_argument_exception.py
"""


class InvalidArgumentException(Exception):
    """Výjimka pro zadání nesprávného argumentu.

    Tato třída reprezentuje zadání uživatelského argumentu, který pro daný nástroj neexistuje, a tudíž je neplatný.
    Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self, msg="An invalid argument is provided.") -> None:
        """**Konstruktor třídy InvalidArgumentException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
