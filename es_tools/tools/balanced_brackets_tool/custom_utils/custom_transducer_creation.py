"""Vytvoření deterministického zobecněného sekvenčního stroje pro odstranění všech znaků vyjma symbolů pro závorky.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci pro vytvoření deterministického zobecněného sekvenčního stroje pro odstranění všech znaků
vyjma symbolů pro závorky.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: custom_transducer_creation.py
"""

from string import printable

from es_tools.formal_models.transducers.deterministic_gsm import DeterministicGeneralizedSequentialMachine
from es_tools.tools.balanced_brackets_tool.custom_utils.brackets_list import brackets_list
from es_tools.tools.balanced_brackets_tool.custom_utils.custom_constants import STATE_NAME


def create_transducer() -> DeterministicGeneralizedSequentialMachine:
    """Vytvoření deterministického zobecněného sekvenčního stroje pro nástroj na ověření vyvážených závorek.

    Tato funkce slouží pro vytvoření deterministického zobecněného sekvenčního stroje pro nástroj na ověření vyvážených
    závorek, přičemž jeho hlavním účelem je převedení vstupního řetězce na takový výstupní řetězec, který obsahují
    pouze symboly závorek.

    :return: vytvořený deterministický zobecněný sekvenční stroj.
    :rtype: DeterministicGeneralizedSequentialMachine
    :raises InvalidTransitionException: neplatný přechod deterministického zobecněného sekvenčního stroje.
    :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů.
    :raises FinalStatesNotStatesSubsetException: množina koncových stavů není podmnožinou množiny stavů.
    """
    ascii_characters = printable

    for bracket in brackets_list:
        ascii_characters = ascii_characters.replace(bracket[0], "")

    transition_relations = list()

    for ascii_character in ascii_characters:
        transition_relations.append((STATE_NAME, ascii_character, STATE_NAME, ""))

    for bracket, complementary_bracket in brackets_list:
        transition_relations.append((STATE_NAME, bracket, STATE_NAME, complementary_bracket))

    initial_state = STATE_NAME
    final_states = {STATE_NAME}

    return DeterministicGeneralizedSequentialMachine(transition_relations, initial_state, final_states)
