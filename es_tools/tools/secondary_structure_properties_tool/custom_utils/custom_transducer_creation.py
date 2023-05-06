"""Vytvoření deterministického zobecněného sekvenčního stroje pro zakódování vstupní sekundární struktury RNA
do požadovaného tvaru dle určených hodnot pro minimum a maximum.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci pro vytvoření deterministického zobecněného sekvenčního stroje pro zakódování vstupní
sekvence RNA do požadovaného tvaru dle určených hodnot pro minimum a maximum.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: custom_transducer_creation.py
"""

from string import ascii_letters

from es_tools.formal_models.transducers.deterministic_gsm import DeterministicGeneralizedSequentialMachine
from es_tools.shared_utils.rna_secondary_structure_unpaired_symbol import unpaired_symbol
from es_tools.tools.secondary_structure_properties_tool.custom_utils.custom_constants import PAIRED_SYMBOL, \
    UNPAIRED_SYMBOL,\
    STATE_NAME


def create_transducer(paired_count: int, unpaired_count: int) -> DeterministicGeneralizedSequentialMachine:
    """Vytvoření deterministického zobecněného sekvenčního stroje pro nástroj na ověření vlastností sekundární
    struktury RNA.

    Tato funkce slouží pro vytvoření deterministického zobecněného sekvenčního stroje pro nástroj na ověření vlastností
    sekundární struktury RNA. Jejím hlavním účelem je zakódování vstupní sekundární struktury RNA do tvaru, kdy řetězec
    obsahuje pouze dva symboly, a to symbol pro párový a symbol pro nepárový nukleotid. Zároveň jsou dodrženy počty
    opakování daného symbolu dle požadované hodnoty minima nebo maxima.

    :param paired_count: počet symbolů pro párový nukleotid dle pravidel pro zakódování řetězce.
    :type paired_count: int
    :param unpaired_count: počet symbolů pro nepárový nukleotid dle pravidel pro zakódování řetězce.
    :type unpaired_count: int
    :return: vytvořený deterministický zobecněný sekvenční stroj.
    :rtype: DeterministicGeneralizedSequentialMachine
    :raises InvalidTransitionException: neplatný přechod deterministického zobecněného sekvenčního stroje.
    :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů.
    :raises FinalStatesNotStatesSubsetException: množina koncových stavů není podmnožinou množiny stavů.
    """
    paired_string = paired_count * PAIRED_SYMBOL
    unpaired_string = unpaired_count * UNPAIRED_SYMBOL

    # Set input symbols of bracket type.
    transition_relations = [(STATE_NAME, "(", STATE_NAME, paired_string),
                            (STATE_NAME, ")", STATE_NAME, paired_string),
                            (STATE_NAME, "[", STATE_NAME, paired_string),
                            (STATE_NAME, "]", STATE_NAME, paired_string),
                            (STATE_NAME, "{", STATE_NAME, paired_string),
                            (STATE_NAME, "}", STATE_NAME, paired_string),
                            (STATE_NAME, "<", STATE_NAME, paired_string),
                            (STATE_NAME, ">", STATE_NAME, paired_string)]

    # Set input symbols from the letters of the alphabet (uppercase and lowercase).
    for letter in list(ascii_letters):
        transition_relations.append((STATE_NAME, letter, STATE_NAME, paired_string))

    for symbol in unpaired_symbol:
        transition_relations.append((STATE_NAME, symbol, STATE_NAME, unpaired_string))

    initial_state = STATE_NAME
    final_states = {STATE_NAME}

    return DeterministicGeneralizedSequentialMachine(transition_relations, initial_state, final_states)
