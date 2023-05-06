"""Vytvoření konečného převodníku pro převod vstupního řešení problému n dam na požadovaný tvar.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci pro vytvoření konečného převodníku, který provádí překlad vstupního řešení problému n dam
na požadovaný tvar, přičemž se jedná především o převod číselných hodnot na symboly řecké abecedy.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: custom_transducer_creation.py
"""

from es_tools.tools.n_queens_problem_tool.custom_utils.custom_constants import FIRST_STATE_NAME, SECOND_STATE_NAME,\
    MAX_BOARD_SIZE
from es_tools.tools.n_queens_problem_tool.custom_utils.english_alphabet import english_alphabet
from es_tools.formal_models.transducers.finite_transducer import FiniteTransducer
from es_tools.shared_utils.greek_alphabet import greek_alphabet


def create_transducer(board_size: int) -> FiniteTransducer:
    """Vytvoření konečného převodníku pro převod vstupního řešení problému n dam na požadovaný tvar.

    Tato funkce slouží pro vytvoření konečného převodníku pro převod vstupního řešení problému n dam na takový tvar, že
    veškeré číselné hodnoty jsou převedeny na symboly řecké abecedy. Zároveň pomocí tohoto převodníku probíhá částečná
    kontrola správnosti tvaru vstupního řetězce.

    :param board_size: rozměr šachovnice pro vstupní řešení.
    :type board_size: int
    :return: vytvořený konečný převodník.
    :rtype: FiniteTransducer
    :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů.
    :raises FinalStatesNotStatesSubsetException: množina koncových stavů není podmnožinou množiny stavů.
    """
    transition_relations = list()
    transitions_count = min(board_size, MAX_BOARD_SIZE)

    for i in range(transitions_count):
        transition_relations.append((FIRST_STATE_NAME, str(i + 1), SECOND_STATE_NAME, greek_alphabet[i]))
        transition_relations.append((SECOND_STATE_NAME, english_alphabet[i], FIRST_STATE_NAME, english_alphabet[i]))

    initial_state = FIRST_STATE_NAME
    final_states = {FIRST_STATE_NAME}

    return FiniteTransducer(transition_relations, initial_state, final_states)
