"""Výjimka pro nekompatibilitu vstupních dat.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že zadaná vstupní data ve vstupním souboru a v rámci
uživatelských argumentů nejsou kompatibilní.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: data_types_not_match_exception.py
"""


class DataTypesNotMatchException(Exception):
    """Výjimka pro nekompatibilitu vstupních dat.

    Tato třída reprezentuje zadání nekompatibilních dat pro typ dat ve vstupním souboru a typ dat zadaných
    jako uživatelské argumenty. Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self,
                 msg="The provided type of input data and the type of the searched sequences do not match.") -> None:
        """**Konstruktor třídy DataTypesNotMatchException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
