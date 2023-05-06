"""Výjimka pro zadání neplatného přechodu převodníku.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že zadané přechody převodníku nejsou platné.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: invalid_transition_exception.py
"""


class InvalidTransitionException(Exception):
    """Výjimka pro zadání neplatného přechodu převodníku.

    Tato třída reprezentuje zadání neplatných přechodů převodníku. Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self, msg="The transitions in the formal model are not valid"
                           "- do not meet the specific requirements.") -> None:
        """**Konstruktor třídy InvalidTransitionException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
