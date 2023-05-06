"""Ověření validity vyhledávaných sekvencí aminokyselin.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci pro ověření validity vyhledávaných sekvencí aminokyselin, přičemž se přirozeně kontroluje,
zda se sekvence skládá pouze z povolených symbolů zastupujících jednotlivé aminokyseliny.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: valid_searched_sequences.py
"""

from typing import List

from es_tools.shared_utils.input_data_check import is_amino_acids_sequence


def valid_searched_sequences(sequences: List[str]) -> bool:
    """Ověření validity sekvencí aminokyselin.

    Tato funkce slouží pro ověření, že se sekvence aminokyselin skládají pouze ze symbolů, které kódují jednotlivé
    aminokyseliny.

    :param sequences: sekvence pro ověření validity.
    :type sequences: List[str]
    :return: určení, zda všechny sekvence jsou validní (True) či nikoliv (False).
    :rtype: bool
    """
    for sequence in sequences:
        if not is_amino_acids_sequence(sequence):
            return False

    return True
