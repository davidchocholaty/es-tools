"""Formální model.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje abstraktní třídu, která je bázovou třídou pro všechny formální modely, jejichž třídy jsou zděděny
od této třídy.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: formal_model.py
"""

from abc import ABC, abstractmethod
from typing import Generator, Union


class FormalModel(ABC):
    """Základní třída pro formální modely.

    Tato abstraktní třída se využívá jako kořenová třída pro všechny formální modely, které dědí od této třídy. Jedinou
    metodou, kterou obsahuje, je metoda run(). Ta slouží především pro zajištění jednotného přístupu spuštění běhu
    zajišťujícího funkcionalitu daného formálního modelu.
    """
    @abstractmethod
    def run(self, input_string: str) -> Union[Generator[str, None, None], bool]:
        """Abstraktní metoda pro spuštění běhu zajišťujícího funkcionality formálního modelu.

        :param input_string: vstupní řetězec.
        :type input_string: str
        :return: v případě převodníku navrací vygenerované výstupní řetězce. Pro vymazávací systém navrací pravdivostní
                 hodnotu určující, zda vstupní řetězec byl přijat či nikoliv.
        :rtype: Union[Generator[str, None, None], bool]
        """
        pass
