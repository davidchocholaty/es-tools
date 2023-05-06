"""Obecný manipulátor.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje definici obecného manipulátoru, přičemž se jedná o základní abstraktní třídu pro vytvoření
manipulátoru pro práci se vstupním souborem nebo pro práci s uživatelskými argumenty.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: handler.py
"""

from abc import ABC, abstractmethod


class Handler(ABC):
    """Definice obecného manipulátoru.

    Tato abstraktní třída slouží jako bázová třída pro třídy, jejichž metody implementují manipulátory zajišťující
    práci se vstupním souborem nebo s uživatelskými argumenty. Jedinou a fundamentální metodou je abstraktní metoda
    handler() ucelující přístup pro získání vytvořeného konkrétního manipulátoru.
    """
    @abstractmethod
    def handler(self):
        """Abstraktní metoda pro navrácení manipulátoru.

        Tato metoda slouží především pro ucelení navrácení vytvořeného manipulátoru v odvozených třídách.
        """
        pass
