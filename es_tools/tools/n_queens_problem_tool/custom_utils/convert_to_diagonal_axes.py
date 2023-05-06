"""Funkce pro převod vstupního řešení problému n dam ze základních souřadnic na souřadnice diagonální.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci pro převod vstupního řešení problému n dam ze základních souřadnic na souřadnice
diagonální.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: convert_to_diagonal_axes.py
"""

from es_tools.shared_utils.greek_alphabet import greek_alphabet
from es_tools.tools.n_queens_problem_tool.custom_utils.english_alphabet import english_alphabet


def convert_to_diagonal_axes(board_size: int, solution_in_base_axes: str) -> str:
    """Převod vstupního řešení problému n dam ze základních souřadnic na souřadnice diagonální.

    Tato funkce provádí převod vstupního řešení problému n dam ze základních souřadnic na souřadnice diagonální.
    Popis algoritmu převodu se v textu práce nachází na stranách 65 a 66, přičemž jsou využity výrazy 6.13 a 6.14.

    :param board_size: rozměr šachovnice pro vstupní řešení.
    :type board_size: int
    :param solution_in_base_axes: vstupní řešení v základních souřadnicích.
    :type solution_in_base_axes: str
    :return: vstupní řešení v diagonálních souřadnicích.
    :rtype: str
    """
    solution_in_diagonal_axes = ""

    for i in range(0, len(solution_in_base_axes), 2):
        old_greek_symbol_index = greek_alphabet.index(solution_in_base_axes[i])
        old_english_symbol_index = english_alphabet.index(solution_in_base_axes[i + 1])

        # V textu výraz 6.13 (g = n + i - j - 1).
        new_greek_symbol_index = board_size + old_greek_symbol_index - old_english_symbol_index - 1
        # V textu výraz 6.14 (e = i + j).
        new_english_symbol_index = old_greek_symbol_index + old_english_symbol_index

        solution_in_diagonal_axes = solution_in_diagonal_axes + \
            greek_alphabet[new_greek_symbol_index] + \
            english_alphabet[new_english_symbol_index]

    return solution_in_diagonal_axes
