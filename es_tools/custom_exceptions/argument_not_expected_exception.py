"""Výjimka pro zadání neočekávaného argumentu.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že zadaný vstupní uživatelský argument nebyl očekáván.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: argument_not_expected_exception.py
"""


class ArgumentNotExpectedException(Exception):
    """Výjimka pro zadání neočekávaného argumentu.

    Tato třída reprezentuje zadání neočekávaného uživatelského argumentu. Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self, msg="An argument was not expected for the specific input data type.") -> None:
        """**Konstruktor třídy ArgumentNotExpectedException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
