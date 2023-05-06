"""Seznam symbolů pro sekundární strukturu RNA.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje seznam všech využitých abeced pro sekundární strukturu RNA. Jedná se nejprve o základní abecedu
obsahující symboly pro závorky. Dále o abecedu, která již obsahuje převedené symboly pro závorky (a nepárové
nukleotidy) na znaky řecké abecedy za účelem minimalizace omezení vymazávacího systému v rámci povolených znaků
pro vymazávací řetězce a regulární jazyky. V poslední řadě tento soubor obsahuje jednotlivé vztahy převodů symbolů
závorek (a nepárových nukleotidů) na znaky řecké abecedy.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: rna_secondary_structure_alphabet.py
"""


rna_secondary_structure_alphabet_base = [
    "(", ")", "[", "]",
    "{", "}", "<", ">",
    "a", "A", "b", "B",
    "c", "C", "d", "D",
    "e", "E", "f", "F",
    "g", "G", "h", "H",
    "i", "I", "j", "J",
    "k", "K", "l", "L",
    "m", "M", "n", "N",
    "o", "O", "p", "P",
    "q", "Q", "r", "R",
    "s", "S", "t", "T",
    "u", "U", "v", "V",
    "w", "W", "x", "X",
    "y", "Y", "z", "Z",
    ".", ":", "|"]

rna_secondary_structure_alphabet_conversed = [
    u"\u03B1", u"\u03B2", u"\u03B3", u"\u03B4",
    u"\u03B5", u"\u03B6", u"\u03B7", u"\u03B8",
    "a", "A", "b", "B",
    "c", "C", "d", "D",
    "e", "E", "f", "F",
    "g", "G", "h", "H",
    "i", "I", "j", "J",
    "k", "K", "l", "L",
    "m", "M", "n", "N",
    "o", "O", "p", "P",
    "q", "Q", "r", "R",
    "s", "S", "t", "T",
    "u", "U", "v", "V",
    "w", "W", "x", "X",
    "y", "Y", "z", "Z",
    u"\u03B9"]

rna_secondary_structure_conversions = {
    "(": u"\u03B1",
    ")": u"\u03B2",
    "[": u"\u03B3",
    "]": u"\u03B4",
    "{": u"\u03B5",
    "}": u"\u03B6",
    "<": u"\u03B7",
    ">": u"\u03B8",
    ".": u"\u03B9",
    ":": u"\u03B9",
    "|": u"\u03B9"}
