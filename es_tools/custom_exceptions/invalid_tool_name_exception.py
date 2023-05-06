"""Výjimka pro zadání neplatného názvu nástroje pro spuštění demonstračního příkladu.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že zadaný název nástroje pro spuštění demonstračního příkladu
není platný.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: invalid_tool_name_exception.py
"""


class InvalidToolNameException(Exception):
    """Výjimka pro zadání neplatného názvu nástroje pro spuštění demonstračního příkladu.

    Tato třída reprezentuje zadání neplatného názvu nástroje. Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self, msg="Invalid tool name. The provided tool does not exist. "
                           "Please check the provided word.") -> None:
        """**Konstruktor třídy InvalidToolNameException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
