"""Výjimka pro zadání neplatných vstupních dat ve vstupním souboru.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že data ve vstupním souboru nejsou platná.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: invalid_input_data_structure_exception.py
"""


class InvalidInputDataStructure(Exception):
    """Výjimka pro zadání neplatných vstupních dat ve vstupním souboru.

    Tato třída reprezentuje zadání nesprávných vstupních dat. Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self, msg="The structure of the input data is not valid.") -> None:
        self.msg = msg
