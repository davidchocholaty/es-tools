"""Ověření validity vyhledávaných sekvencí.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci, která ověřuje validitu vyhledávaných sekvencí.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: valid_searched_sequences.py
"""

from typing import List, Tuple

from es_tools.shared_utils.input_data_check import is_rna_sequence, is_dna_sequence, \
    is_rna_secondary_structure_subsequence
from es_tools.tools.sequence_search_tool.custom_utils.data_type import DataType


def valid_searched_sequences(sequences: List[str]) -> Tuple[bool, DataType]:
    """Ověření validity vyhledávaných sekvencí.

    Tato funkce slouží pro ověření validity vyhledávaných sekvencí. Je tudíž ověřeno, zda všechny vyhledávané sekvence
    jsou stejného datového typu, přičemž se může jednat o DNA, RNA podsekvence nebo podsekvence sekundárních struktur
    RNA. Zároveň je provedena kontrola shody datového typu podsekvencí s datovým typem vstupní sekvence.

    :param sequences: seznam sekvencí pro ověření validity. To znamená, že je ověřeno, zda všechny vyhledávané
                      podsekvence jsou totožného povoleného datového typu a že se daný datový typ shoduje s datovým
                      typem vstupní sekvence, ve které mají být podsekvence vyhledávány.
    :type sequences: List[str]
    :return: pravdivostní hodnota určující validitu vyhledávaných sekvencí a společný datový typ podsekvencí.
    :rtype: Tuple[bool, DataType]
    """
    if len(sequences) > 0:
        if is_rna_sequence(sequences[0]):
            if is_dna_sequence(sequences[0]):
                chosen_structure_type = DataType.RNA_OR_DNA_SEQUENCE
            else:
                chosen_structure_type = DataType.RNA_SEQUENCE
        elif is_dna_sequence(sequences[0]):
            chosen_structure_type = DataType.DNA_SEQUENCE
        elif is_rna_secondary_structure_subsequence(sequences[0]):
            chosen_structure_type = DataType.RNA_SECONDARY_STRUCTURE_SEQUENCE
        else:
            return False, DataType.UNSET

        for i in range(1, len(sequences)):
            if is_rna_sequence(sequences[i]):
                if is_dna_sequence(sequences[i]):
                    if chosen_structure_type == DataType.RNA_SECONDARY_STRUCTURE_SEQUENCE:
                        return False, DataType.UNSET
                elif chosen_structure_type == DataType.RNA_OR_DNA_SEQUENCE:
                    chosen_structure_type = DataType.RNA_SEQUENCE
                elif chosen_structure_type != DataType.RNA_SEQUENCE:
                    return False, DataType.UNSET
            elif is_dna_sequence(sequences[i]):
                if chosen_structure_type == DataType.RNA_OR_DNA_SEQUENCE:
                    chosen_structure_type = DataType.DNA_SEQUENCE
                elif chosen_structure_type != DataType.DNA_SEQUENCE:
                    return False, DataType.UNSET
            elif is_rna_secondary_structure_subsequence(sequences[i]):
                if chosen_structure_type != DataType.RNA_SECONDARY_STRUCTURE_SEQUENCE:
                    return False, DataType.UNSET
            else:
                return False, DataType.UNSET

        return True, chosen_structure_type

    return False, DataType.UNSET
