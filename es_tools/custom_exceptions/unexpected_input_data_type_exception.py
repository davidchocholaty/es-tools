"""Výjimka pro neočekávaný typ vstupních dat.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že byl zadán neočekávaný či nekompatibilní typ vstupních dat.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: unexpected_input_data_type_exception.py
"""


class UnexpectedInputDataTypeException(Exception):
    """Výjimka pro neočekávaný typ vstupních dat.

    Tato třída reprezentuje zadání neočekávaného či nekompatibilního typu vstupních dat. Jako výjimka je odvozena
    od třídy Exception.
    """
    def __init__(self, msg="The input data type does not match one of the expected types.") -> None:
        """**Konstruktor třídy UnexpectedInputDataTypeException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
