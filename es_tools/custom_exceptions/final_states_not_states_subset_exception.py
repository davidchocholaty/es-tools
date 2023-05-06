"""Výjimka pro neplatnou množinu koncových stavů převodníku.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že zadaná množina koncových stavů není dle definice platná.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: final_states_not_states_subset_exception.py
"""


class FinalStatesNotStatesSubsetException(Exception):
    """Výjimka pro neplatnou množinu koncových stavů.

    Tato třída reprezentuje zadání neplatné množiny koncových stavů převodníku, přičemž tato množina není podmnožinou
    množiny všech stavů převodníku. Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self, msg="Final states are not a subset of states.") -> None:
        """**Konstruktor třídy FinalStatesNotStatesSubsetException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
