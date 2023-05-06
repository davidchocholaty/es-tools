"""Povolené datové typy vstupních sekvencí.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje výčet možných datových typů vstupní sekvence pro vyhledávání podsekvencí. Vstupní řetězec může
reprezentovat RNA sekvenci, sekundární strukturu RNA. V případě dvou vstupních řetězců můžou tyto řetězce reprezentovat
vlákna DNA sekvence. Pokud vstupní sekvence neobsahuje bázi specifickou pro RNA nebo DNA, tedy uracil nebo thymin,
tak se uvažuje datový typ určující, že se jedná o RNA nebo DNA (RNA_OR_DNA_SEQUENCE).

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: data_type.py
"""

from enum import Enum


class DataType(Enum):
    """Výčet možných datových typů sekvencí."""
    UNSET = 0
    """
    Datový typ sekvence není nastaven (výchozí hodnota).
    """
    RNA_SEQUENCE = 1
    """
    RNA sekvence.
    """
    DNA_SEQUENCE = 2
    """
    DNA sekvence.
    """
    RNA_SECONDARY_STRUCTURE_SEQUENCE = 3
    """
    Sekvence sekundární struktury RNA.
    """
    RNA_OR_DNA_SEQUENCE = 4
    """
    Vstupní sekvence může být DNA nebo RNA sekvence, přičemž dle zadaných nukleotidů není možné přesně určit typ
    (sekvence neobsahuje bázi uracilu nebo thyminu).
    """
