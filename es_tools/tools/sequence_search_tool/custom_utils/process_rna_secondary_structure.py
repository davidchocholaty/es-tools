"""Vyhledávání podsekvencí v sekvenci sekundární struktury RNA.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci, která implementuje hlavní algoritmus pro vyhledávání podsekvencí v sekvenci sekundární
struktury RNA.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: process_rna_secondary_structure.py
"""

from typing import List

from es_tools.custom_exceptions.final_states_not_states_subset_exception import FinalStatesNotStatesSubsetException
from es_tools.custom_exceptions.illegal_symbol_occurrence_exception import IllegalSymbolOccurrenceException
from es_tools.custom_exceptions.initial_state_not_in_states_exception import InitialStateNotInStatesException
from es_tools.custom_exceptions.invalid_regular_language_pattern_exception import InvalidRegularLanguagePatternException
from es_tools.custom_exceptions.maximum_input_string_length_exceeded_exception import \
    MaximumInputStringLengthExceededException
from es_tools.tools.sequence_search_tool.custom_utils.process_sequence import process_sequence
from es_tools.shared_utils.rna_secondary_structure_alphabet \
    import rna_secondary_structure_alphabet_conversed, rna_secondary_structure_conversions


def process_rna_secondary_structure(input_sequence: str,
                                    sequences: List[str],
                                    greedy_quantifier: bool,
                                    verbose: bool) -> None:
    """Vyhledávání sekvencí v sekundární struktuře RNA.

    :param input_sequence: vstupní sekvence sekundární struktury RNA.
    :param sequences: vyhledávané sekvence v sekundární struktuře RNA.
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
    print("Input RNA secondary structure sequence: " + input_sequence + "\n")
    print("Searched sequences: " + str(sequences)[1:-1])

    for i in range(len(input_sequence)):
        if input_sequence[i] in rna_secondary_structure_conversions:
            input_sequence = input_sequence[:i] +\
                             rna_secondary_structure_conversions[input_sequence[i]] +\
                             input_sequence[i + 1:]

    for j in range(len(sequences)):
        for i in range(len(sequences[j])):
            if sequences[j][i] in rna_secondary_structure_conversions:
                sequences[j] = sequences[j][:i] + \
                               rna_secondary_structure_conversions[sequences[j][i]] + \
                               sequences[j][i + 1:]

    alphabet = rna_secondary_structure_alphabet_conversed

    try:
        accepted = process_sequence(input_sequence, sequences, alphabet, greedy_quantifier, verbose)
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
        print("### Input RNA secondary structure sequence meets the requirements ###")
    else:
        print("------------------------------------------------------------------------------------\n")
        print("### Input RNA secondary structure sequence does not meet the requirements ###")
