"""Chybové návratové kódy.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje chybové návratové kódy společné i specifické pro jednotlivé nástroje a pro skripty spouštějící
ukázkové příklady.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: exit_code.py
"""

from enum import Enum


class ExitCode(Enum):
    """Výčet chybových kódů.

    Tato třída obsahuje výčet všech použitých chybových stavů, přičemž je zděděna od rodičovské třídy Enum.
    """
    WRONG_ARGUMENT = 10
    """
    Zadání neexistujícího argumentu.
    """
    INVALID_ARGUMENT_VALUE = 11
    """
    Hodnota argumentu není validní.
    """
    REQUIRED_ARGUMENT_NOT_PROVIDED = 12
    """
    Požadovaný argument nebyl zadán.
    """
    FILE_NOT_FOUND = 20
    """
    Zadaný vstupní soubor nebyl nalezen.
    """
    INVALID_INPUT_DATA_STRUCTURE = 21
    """
    Struktura dat ve vstupním souboru není validní.
    """
    INVALID_INPUT_DATA_TYPE = 22
    """
    Typ vstupních dat není validní.
    """
    INITIAL_STATE_NOT_IN_STATES = 30
    """
    Počáteční stav převodníku nenáleží do množiny všech stavů.
    """
    FINAL_STATES_NOT_STATES_SUBSET = 31
    """
    Množina koncových stavů není podmnožinou množiny všech stavů.
    """
    INVALID_TRANSITION = 32
    """
    Zadání neplatného přechodu převodníku.
    """
    INVALID_ERASING_STRING = 40
    """
    Zadání vymazávacího řetězce obsahujícího zakázaný symbol.
    """
    INVALID_REGULAR_LANGUAGE = 41
    """
    Zadání regulárního jazyka vymazávacího systému, jehož tvar není validní nebo povolený.
    """
    MAXIMUM_INPUT_STRING_LENGTH_EXCEEDED = 42
    """
    Překročena maximální povolená délka vstupního řetězce pro zpracování vymazávacím systémem.
    """
    INVALID_EXAMPLE_NUMBER = 70
    """
    Zadané číslo ukázkového příkladu pro příslušný nástroj neexistuje.
    """
    UNKNOWN_PLATFORM_SYSTEM = 80
    """
    Neznámý operační systém, na kterém je spuštěn ukázkový příklad.
    """
    INTERNAL_ERROR = 99
    """
    Neočekávaná vnitřní chyba programu.
    """
