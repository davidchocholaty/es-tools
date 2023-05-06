"""Výjimka pro překročení maximální povolené délky vstupního řetězce.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výjimku sloužící pro reprezentaci, že byla překročena maximální povolená délka vstupního řetězce.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: maximum_input_string_length_exceeded_exception.py
"""


class MaximumInputStringLengthExceededException(Exception):
    """Výjimka pro překročení maximální povolené délky vstupního řetězce.

    Tato třída reprezentuje zadání vstupního řetězce, který překračuje maximální povolenou délku vstupního řetězce.
    Jako výjimka je odvozena od třídy Exception.
    """
    def __init__(self, msg="The provided input string is longer than the allowed maximum length.") -> None:
        """**Konstruktor třídy MaximumInputStringLengthExceededException**

        :param msg: chybová zpráva.
        :type msg: str
        """
        self.msg = msg
