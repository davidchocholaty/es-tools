"""Nástroje pro kontrolu vstupních dat.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje utility pro kontrolu vstupních dat, a to především sekvencí z oblasti molekulární biologie, jako
je DNA, RNA sekvence, sekundární struktura RNA či sekvence aminokyselin.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: input_data_check.py
"""

import re

from es_tools.shared_utils.amino_acids_list import amino_acids_list
from es_tools.shared_utils.nucleotides_list import nucleotides_rna, nucleotides_dna
from es_tools.shared_utils.rna_secondary_structure_alphabet import rna_secondary_structure_alphabet_base
from es_tools.shared_utils.rna_secondary_structure_unpaired_symbol import unpaired_symbol


def is_rna_sequence(sequence: str) -> bool:
    """Funkce pro ověření, zda vstupní řetězec je RNA sekvence.

    Funkce slouží pro ověření, zda vstupní řetězec je sekvence RNA, přičemž se může skládat pouze z ribonukleotidů.

    :param sequence: vstupní řetězec pro ověření, zda se jedná o RNA sekvenci.
    :type sequence: str
    :return: True, pokud vstupní řetězec je RNA sekvence, jinak False.
    :rtype: bool
    """
    pattern = "[" + "".join(nucleotides_rna) + "]*"

    if re.fullmatch(pattern, sequence):
        return True

    return False


def is_rna_secondary_structure_subsequence(subsequence: str) -> bool:
    """Funkce pro ověření, zda vstupní řetězec je podsekvence sekundární struktury RNA.

    Tato funkce slouží pro ověření, zda poskytnutý řetězec reprezentuje podsekvenci sekundární struktury RNA, přičemž
    se kontrolují pouze symboly dle definované abecedy a zda řetězec obsahuje pouze jeden akceptovaný symbol
    pro nepárové nukleotidy. Narozdíl od funkce is_rna_secondary_structure_sequence() pro podsekvenci není prováděna
    kontrola vzájemného párování párových nukleotidů.

    :param subsequence: vstupní řetězec pro ověření, zda se jedná o podsekvenci sekundární struktury RNA.
    :type subsequence: str
    :return: True, pokud vstupní řetězec je podsekvence sekundární struktury RNA, jinak False.
    :rtype: bool
    """
    chosen_unpaired_symbol = ""

    for symbol in subsequence:
        if symbol in rna_secondary_structure_alphabet_base:
            if symbol in unpaired_symbol:
                if chosen_unpaired_symbol == "":
                    chosen_unpaired_symbol = symbol
                elif symbol != chosen_unpaired_symbol:
                    return False
        else:
            return False

    return True


def is_rna_secondary_structure_sequence(sequence: str) -> bool:
    """Funkce pro ověření, zda vstupní řetězec je sekundární struktura RNA.

    Tato funkce slouží pro ověření, zda vstupní řetězec je sekundární struktura RNA, přičemž se může skládat pouze ze
    symbolů pro závorky, znaků anglické abecedy či akceptovaných symbolů pro nepárové nukleotidy. Zároveň probíhá
    kontrola správného párování jednotlivých nukleotidů v tom ohledu, že se kontroluje, zda se řetězec v případě
    párových nukleotidů skládá pouze z komplementárních dvojic.

    :param sequence: vstupní řetězec pro ověření, zda se jedná o sekundární strukturu RNA.
    :type sequence: str
    :return: True, pokud vstupní řetězec je sekundární struktura RNA, jinak False.
    :rtype: bool
    """
    complementary_symbols = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
        "a": "A",
        "b": "B",
        "c": "C",
        "d": "D",
        "e": "E",
        "f": "F",
        "g": "G",
        "h": "H",
        "i": "I",
        "j": "J",
        "k": "K",
        "l": "L",
        "m": "M",
        "n": "N",
        "o": "O",
        "p": "P",
        "q": "Q",
        "r": "R",
        "s": "S",
        "t": "T",
        "u": "U",
        "v": "V",
        "w": "W",
        "x": "X",
        "y": "Y",
        "z": "Z"}

    loaded_symbols = []
    chosen_unpaired_symbol = ""

    for symbol in sequence:
        if symbol in complementary_symbols.values():  # otevírací závorka
            loaded_symbols.append(symbol)
        elif symbol in complementary_symbols:  # uzavírací závorka
            try:
                loaded_symbol_index = "".join(loaded_symbols).rindex(complementary_symbols[symbol])
            except ValueError:
                loaded_symbols.clear()
                return False

            # Odstranění posledního výskytu komplementárního symbolu.
            del loaded_symbols[loaded_symbol_index]

        elif symbol in unpaired_symbol:
            if chosen_unpaired_symbol == "":
                chosen_unpaired_symbol = symbol
            elif symbol != chosen_unpaired_symbol:
                loaded_symbols.clear()
                return False
        else:
            loaded_symbols.clear()
            return False

    return not loaded_symbols


def is_dna_sequence(sequence: str) -> bool:
    """Funkce pro ověření, zda vstupní řetězec je DNA vlákno.

    Tato funkce slouží pro ověření, zda poskytnutý vstupní řetězec je vlákno DNA, přičemž se kontroluje, jestli
    se zkládá pouze z deoxyribonukleotidů.

    :param sequence: vstupní řetězec pro ověření, zda se jedná o jedno ze dvou vláken DNA (může se skládat pouze
                     z deoxyribonukleotidů).
    :type sequence: str
    :return: True, pokud vstupní řetězec je vlákno DNA, jinak False.
    :rtype: bool
    """
    pattern = "[" + "".join(nucleotides_dna) + "]*"

    if re.fullmatch(pattern, sequence):
        return True

    return False


def is_dna_double_stranded_sequence(strand_5_3: str, strand_3_5: str) -> bool:
    """Funkce pro ověření, zda řetězce jsou komplementární vlákna DNA.

    Tato funkce slouží pro ověření, zda dva poskytnuté řetězce reprezentují dvě komplementární vlákna DNA (přičemž
    jedno je takzvaně antiparalerní k druhému). Nejprve probíhá kontrola jejich délky, poté se kontroluje, zda se
    skládájí pouze z deoxyribonukleotidů zároveň s probíhající kontrolou jejich vzájemné komplementarity.

    :param strand_5_3: řetězec reprezentující vlákno DNA ve směru 5'->3'.
    :type strand_5_3: str
    :param strand_3_5: řetězec reprezentující vlákno DNA ve směru 3'->5'.
    :type strand_3_5: str
    :return: True, pokud vstupní řetězce jsou dvě komplementární vlákna jedné DNA, jinak False.
    :rtype: bool
    """
    # Kontrola shodné délky obou vláken.
    strand_5_3_length = len(strand_5_3)
    strand_3_5_length = len(strand_3_5)

    if strand_5_3_length != strand_3_5_length:
        return False

    dna_complementary_bases = {"A": "T",
                               "T": "A",
                               "G": "C",
                               "C": "G"}

    # Kontrola symbolů a komplementarity obou vláken.
    for i in range(strand_5_3_length):
        if strand_5_3[i] in dna_complementary_bases:
            if dna_complementary_bases[strand_5_3[i]] != strand_3_5[i]:
                return False
        else:
            return False

    return True


def is_amino_acids_sequence(sequence: str) -> bool:
    """ Funkce pro ověření, zda vstupní řetězec je sekvence aminokyselin.

    Tato funkce slouží pro ověření, zda poskytnutý řetězec se skládá pouze z definovaných aminokyselin.

    :param sequence: vstupní řetězec pro ověření, zda se jedná o sekvenci aminokyselin.
    :type sequence: str
    :return: True, pokud vstupní řetězec je sekvence aminokyselin, jinak False.
    :rtype: bool
    """
    pattern = "[" + "".join(amino_acids_list) + "]*"

    if re.fullmatch(pattern, sequence):
        return True

    return False
