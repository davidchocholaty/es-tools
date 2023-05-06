"""Výjimka pro zadání neplatné vyhledávané sekvence ve formě uživatelského argumentu.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že zadaná vyhledávaná sekvence ve formě vstupního argumentu
není platná.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: invalid_searched_sequences_exception.py
"""


class InvalidSearchedSequencesException(Exception):
    """Výjimka pro zadání neplatné vyhledávané sekvence ve formě uživatelského argumentu.

    Tato třída reprezentuje zadání neplatné vyhledávané sekvence. Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self, msg="Invalid search sequences. The provided sequences generally do not match "
                           "the expected structure") -> None:
        """**Konstruktor třídy InvalidSearchedSequencesException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
