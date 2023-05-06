"""Vyhledávání podsekvencí v RNA sekvenci.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci, která implementuje hlavní algoritmus pro vyhledávání podsekvencí v RNA sekvenci.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: process_rna_sequence.py
"""

from typing import List

from es_tools.custom_exceptions.final_states_not_states_subset_exception import FinalStatesNotStatesSubsetException
from es_tools.custom_exceptions.illegal_symbol_occurrence_exception import IllegalSymbolOccurrenceException
from es_tools.custom_exceptions.initial_state_not_in_states_exception import InitialStateNotInStatesException
from es_tools.custom_exceptions.invalid_regular_language_pattern_exception import InvalidRegularLanguagePatternException
from es_tools.custom_exceptions.maximum_input_string_length_exceeded_exception import \
    MaximumInputStringLengthExceededException
from es_tools.shared_utils.nucleotides_list import nucleotides_rna
from es_tools.tools.sequence_search_tool.custom_utils.process_sequence import process_sequence


def process_rna_sequence(input_sequence: str, sequences: List[str], greedy_quantifier: bool, verbose: bool) -> None:
    """Vyhledávání podsekvencí v RNA sekvenci.

    :param input_sequence: vstupní RNA sekvence.
    :param sequences: vyhledávané podsekvence v RNA sekvenci.
    :param greedy_quantifier: typ kvantifikátoru (True — chamtivý, False — líný).
    :type greedy_quantifier: bool
    :param verbose: určení, zda mají být vypisovány na standardní výstup při činnosti vymazávacího systému podrobné
                    informace.
    :type verbose: bool
    :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů.
    :raises FinalStatesNotStatesSubsetException: množina koncových stavů není podmnožinou množiny stavů.
    :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci.
    :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního výrazu
                                                    pro regulární jazyk.
    :raises MaximumInputStringLengthExceededException: překročena maximální povolená délka vstupního řetězce pro
                                                       vymazávací systém.
    """
    print("Input RNA sequence: " + input_sequence + "\n")
    print("Searched sequences: " + str(sequences)[1:-1])

    try:
        accepted = process_sequence(input_sequence, sequences, nucleotides_rna, greedy_quantifier, verbose)
    except InitialStateNotInStatesException:
        raise
    except FinalStatesNotStatesSubsetException:
        raise
    except IllegalSymbolOccurrenceException:
        raise
    except InvalidRegularLanguagePatternException:
        raise
    except MaximumInputStringLengthExceededException:
        raise

    if accepted:
        print("------------------------------------------------------------------------------------\n")
        print("### Input RNA sequence meets the requirements ###")
    else:
        print("------------------------------------------------------------------------------------\n")
        print("### Input RNA sequence does not meet the requirements ###")
