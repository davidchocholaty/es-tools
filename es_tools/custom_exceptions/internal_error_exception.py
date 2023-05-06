"""Výjimka pro reprezentaci interní chyby.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že během běhu aplikace se vyskytla neočekávaná interní chyba.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: internal_error_exception.py
"""


class InternalErrorException(Exception):
    """Výjimka pro reprezentaci interní chyby.

    Tato třída reprezentuje situaci, kdy nastane interní chyba, přičemž není možné další vykonávání programu.
    Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self, msg="An internal program error has occurred.") -> None:
        """**Konstruktor třídy InternalErrorException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
