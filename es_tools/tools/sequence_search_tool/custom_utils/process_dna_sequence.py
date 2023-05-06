"""Vyhledávání podsekvencí ve vláknech DNA.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci, která implementuje hlavní algoritmus pro vyhledávání podsekvencí ve dvou vláknech DNA.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: process_dna_sequence.py
"""

from typing import List

from es_tools.custom_exceptions.final_states_not_states_subset_exception import FinalStatesNotStatesSubsetException
from es_tools.custom_exceptions.illegal_symbol_occurrence_exception import IllegalSymbolOccurrenceException
from es_tools.custom_exceptions.initial_state_not_in_states_exception import InitialStateNotInStatesException
from es_tools.custom_exceptions.internal_error_exception import InternalErrorException
from es_tools.custom_exceptions.invalid_regular_language_pattern_exception import InvalidRegularLanguagePatternException
from es_tools.custom_exceptions.maximum_input_string_length_exceeded_exception import \
    MaximumInputStringLengthExceededException
from es_tools.shared_utils.nucleotides_list import nucleotides_dna
from es_tools.tools.sequence_search_tool.custom_utils.process_sequence import process_sequence
from es_tools.tools.sequence_search_tool.custom_utils.data_type import DataType


def process_dna_sequence(strands: List[str],
                         sequences: List[str],
                         dna_type: str,
                         greedy_quantifier: bool,
                         verbose: bool) -> None:
    """Vyhledávání sekvencí ve dvou vláknech DNA.

    Tato funkce slouží pro vyhledávání sekvencí ve dvou vláknech DNA. Na základě typu vyhledávání je případně provedena
    reverzace druhého vlákna DNA.

    :param strands: seznam obsahující dvě položky, a to jednotlivá vlákna DNA.
    :type strands: List[str]
    :param sequences: vyhledávané sekvence ve vláknech DNA.
    :type sequences: List[str]
    :param dna_type: typ vyhledávání ve vláknech DNA.
    :type dna_type: str
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
    accepted = False

    if len(strands) != DataType.DNA_SEQUENCE.value:
        raise InternalErrorException

    print("Input DNA strand 5->3: " + strands[0] + "\n")
    print("Input DNA strand 3->5: " + strands[1] + "\n")
    print("Searched sequences: " + str(sequences)[1:-1])
    print("DNA search type: " + dna_type)

    if dna_type in ["35", "both", ""]:
        # Reverse the second strand for searching.
        strands[1] = strands[1][::-1]

    if dna_type == "53":
        del strands[1]
    elif dna_type == "35" or dna_type == "35_reversed":
        del strands[0]

    i = 0
    while i < len(strands) and not accepted:
        try:
            accepted = process_sequence(strands[i], sequences, nucleotides_dna, greedy_quantifier, verbose)
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

        i = i + 1

    if accepted:
        print("------------------------------------------------------------------------------------\n")
        print("### Input DNA sequences meets the requirements ###")
    else:
        print("------------------------------------------------------------------------------------\n")
        print("### Input DNA sequences does not meet the requirements ###")
