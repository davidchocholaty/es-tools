"""Výjimka pro nezadání požadovaného argumentu.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že požadovaný vstupní uživatelský argument nebyl zadán.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: required_argument_not_provided_exception.py
"""


class RequiredArgumentNotProvidedException(Exception):
    """Výjimka pro nezadání požadovaného argumentu.

    Tato třída reprezentuje situaci, kdy nebyl zadán požadovaný vstupní uživatelnský argument.  Jako výjimka
    je odvozena od třídy Exception.

    """
    def __init__(self, msg="The required argument was not provided.") -> None:
        """**Konstruktor třídy RequiredArgumentNotProvidedException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
