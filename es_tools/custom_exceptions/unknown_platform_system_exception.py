"""Výjimka pro neznámý operační systém.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že operační systém není rozpoznán.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: unknown_platform_system_exception.py
"""


class UnknownPlatformSystemException(Exception):
    """Výjimka pro neznámý operační systém.

    Tato třída reprezentuje výjimku pro neznámý operační systém. Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self, msg="The unknown operation system. Expected one of the following: "
                           "Linux, Darwin (macOS), Windows") -> None:
        """**Konstruktor třídy UnknownPlatformSystemException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
