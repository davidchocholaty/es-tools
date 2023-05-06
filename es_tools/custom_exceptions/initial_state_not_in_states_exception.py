"""Výjimka pro zadání neplatného počátečního stavu převodníku.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že zadaný počáteční stav převodníku není platný.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: initial_state_not_in_states_exception.py
"""


class InitialStateNotInStatesException(Exception):
    """Výjimka pro zadání neplatného počátečního stavu převodníku.

    Tato třída reprezentuje zadání počátečního stavu, který nesplňuje tu podmínku, že náleží do množiny stavů
    převodníku. Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self, msg="Initial state is not in the set of states.") -> None:
        """**Konstruktor třídy InitialStateNotInStatesException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
