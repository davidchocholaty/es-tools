"""Vyhledávání podsekvencí ve vstupní sekvenci.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci, která implementuje hlavní algoritmus pro vyhledávání podsekvencí ve vstupní sekvenci.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: process_sequence.py
"""

from typing import List

from es_tools.custom_exceptions.final_states_not_states_subset_exception import FinalStatesNotStatesSubsetException
from es_tools.custom_exceptions.illegal_symbol_occurrence_exception import IllegalSymbolOccurrenceException
from es_tools.custom_exceptions.initial_state_not_in_states_exception import InitialStateNotInStatesException
from es_tools.custom_exceptions.invalid_regular_language_pattern_exception import InvalidRegularLanguagePatternException
from es_tools.custom_exceptions.maximum_input_string_length_exceeded_exception import \
    MaximumInputStringLengthExceededException
from es_tools.shared_utils.transducer_creation_sequences_labelling import create_transducer_subsequences_labelling
from es_tools.tools.sequence_search_tool.custom_utils.custom_erasing_system_creation import create_custom_erasing_system
from es_tools.shared_utils.shared_constants import SUBSEQUENCE_LABEL


def process_sequence(input_sequence: str,
                     sequences: List[str],
                     alphabet: List[str],
                     greedy_quantifier: bool,
                     verbose: bool) -> bool:
    """Vyhledávání podsekvencí ve vstupní sekvenci.

    Tato funkce slouží pro vyhledávání nepřekrývajících se výskytů všech podsekvencí ve vstupní sekvenci, přičemž
    se uvažuje vyhledávání nezávislé na datovém typu vstupní sekvence a podsekvencí.

    :param input_sequence: vstupní sekvence.
    :param sequences: vyhledávané podsekvence ve vstupní sekvenci.
    :param greedy_quantifier: typ kvantifikátoru (True — chamtivý, False — líný).
    :type greedy_quantifier: bool
    :param verbose: určení, zda mají být vypisovány na standardní výstup při činnosti vymazávacího systému podrobné
                    informace.
    :type verbose: bool
    :return: určení, zda vstupní sekvence obsahuje všechny nepřekrývající se výskyty vyhledávaných podsekvencí (True)
             či nikoliv (False).
    :rtype: bool
    :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů.
    :raises FinalStatesNotStatesSubsetException: množina koncových stavů není podmnožinou množiny stavů.
    :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci.
    :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního výrazu
                                                    pro regulární jazyk.
    :raises MaximumInputStringLengthExceededException: překročena maximální povolená délka vstupního řetězce pro
                                                       vymazávací systém.
    """
    try:
        transducer = create_transducer_subsequences_labelling(alphabet, sequences)
    except InitialStateNotInStatesException:
        raise
    except FinalStatesNotStatesSubsetException:
        raise

    generated_output_strings = transducer.run(input_sequence)
    output_strings = list(generated_output_strings)

    output_strings_with_labels_count = {}
    searched_sequences_number = len(sequences)

    for output_string in output_strings:
        labels_count = output_string.count(SUBSEQUENCE_LABEL)

        if labels_count >= searched_sequences_number:
            output_strings_with_labels_count.update({output_string: labels_count})

    if len(output_strings_with_labels_count) == 0:
        return False

    # Následující řádek kódu je převzat:
    #
    # Zdrojový web: Stack Overflow.
    # Odkaz na původní otázku: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    # Autor otázky: Gern Blanston (https://stackoverflow.com/users/2786/gern-blanston).
    # Otázka upravena: Anvesh (https://stackoverflow.com/users/8850745/anvesh).
    # Autor odpovědi: Devin Jeanpierre (https://stackoverflow.com/users/18515/devin-jeanpierre).
    # Odpověď upravena: wjandrea (https://stackoverflow.com/users/4518341/wjandrea).
    #
    # *** Začátek převzatého kódu. ***
    output_strings_with_labels_count = {key: value for key, value in sorted(output_strings_with_labels_count.items(),
                                                                            key=lambda item: item[1], reverse=True)}
    # *** Konec převzatého kódu. ***

    try:
        erasing_system = create_custom_erasing_system(sequences, greedy_quantifier, verbose)
    except IllegalSymbolOccurrenceException:
        raise
    except InvalidRegularLanguagePatternException:
        raise

    for output_string in output_strings_with_labels_count.keys():
        try:
            if erasing_system.run(output_string):
                return True
        except MaximumInputStringLengthExceededException:
            raise

    return False
