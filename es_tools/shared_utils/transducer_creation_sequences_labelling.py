"""Vytvoření převodníku pro označování podsekvencí.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje sdílenou funkci zajišťující vytvoření převodníku pro označování podsekvencí vstupní sekvence.
Tuto funkci využívá nástroj SequencesSearchTool a nástroj AminoAcidSequenceSearchTool.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: transducer_creation_sequences_labelling.py
"""

from typing import List

from es_tools.formal_models.transducers.finite_transducer import FiniteTransducer
from es_tools.shared_utils.shared_constants import SUBSEQUENCE_LABEL

STATE_NAME = "s"


def create_transducer_subsequences_labelling(input_symbols: List[str], subsequences: List[str]) -> FiniteTransducer:
    """Převodník pro označení a převedení podsekvencí.

    Tato funkce slouží pro vytvoření převodníku pro označení zadaných podsekvencí a převedení všech možných
    jednotlivých vstupních symbolů na prázdný řetězec (epsilon).

    :param input_symbols: veškeré možné vstupní symboly (abeceda).
    :type input_symbols: List[str]
    :param subsequences: seznam podsekvencí, které mají být s označením zapsány na výstupní pásku.
    :type subsequences: List[str]
    :return: vytvořený konečný převodník pro označení zadaných podsekvencí.
    :rtype: FiniteTransducer
    """
    transition_relations = list()

    for symbol in input_symbols:
        transition_relations.append((STATE_NAME, symbol, STATE_NAME, ""))

    for subsequence in subsequences:
        transition_relations.append((STATE_NAME, subsequence, STATE_NAME, SUBSEQUENCE_LABEL + subsequence))

    initial_state = STATE_NAME
    final_states = {STATE_NAME}

    return FiniteTransducer(transition_relations, initial_state, final_states)
