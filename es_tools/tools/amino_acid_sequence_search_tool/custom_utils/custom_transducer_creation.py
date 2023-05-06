"""Vytvoření konečného převodníku pro převod sekvence RNA na sekvenci proteinů.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje funkci pro vytvoření konečného převodníku, který provádí překlad vstupní sekvence RNA na sekvenci
proteinů.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: custom_transducer_creation.py
"""

from es_tools.formal_models.transducers.finite_transducer import FiniteTransducer
from es_tools.tools.amino_acid_sequence_search_tool.custom_utils.custom_constants import FIRST_STATE_NAME,\
    SECOND_STATE_NAME, THIRD_STATE_NAME, FOURTH_STATE_NAME, PROTEIN_START_LABEL, PROTEIN_END_LABEL


def create_transducer_triplets_processing(non_terminated: bool) -> FiniteTransducer:
    """Vytvoření konečného převodníku pro translaci prokaryotické sekvence RNA na sekvenci proteinů.

    Tato funkce slouží pro vytvoření konečného převodníku pro translaci prokaryotické sekvence RNA na sekvenci
    proteinů, přičemž je možné určit, zda může RNA sekvence obsahovat na svém konci protein, který není zakončen
    takzvaným stop kodonem.

    :param non_terminated: určení, zda může RNA sekvence končit i proteinem, který není ukončen takzvaným stop kodonem,
                           přičemž je dodržený převod po trojicích nukleotidů.
    :type non_terminated: bool
    :return: vytvořený konečný převodník.
    :rtype: FiniteTransducer
    :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů.
    :raises FinalStatesNotStatesSubsetException: množina koncových stavů není podmnožinou množiny stavů.
    """
    transition_relations = list()

    # Přidání jednotlivých nukleotidů.
    transition_relations.append((FIRST_STATE_NAME, "U", FIRST_STATE_NAME, ""))
    transition_relations.append((FIRST_STATE_NAME, "G", FIRST_STATE_NAME, ""))
    transition_relations.append((FIRST_STATE_NAME, "C", FIRST_STATE_NAME, ""))

    # Start kodon - první nukleotid.
    transition_relations.append((FIRST_STATE_NAME, "A", SECOND_STATE_NAME, ""))

    transition_relations.append((SECOND_STATE_NAME, "A", SECOND_STATE_NAME, ""))

    transition_relations.append((SECOND_STATE_NAME, "G", FIRST_STATE_NAME, ""))
    transition_relations.append((SECOND_STATE_NAME, "C", FIRST_STATE_NAME, ""))

    # Start kodon - druhý nukleotid.
    transition_relations.append((SECOND_STATE_NAME, "U", THIRD_STATE_NAME, ""))

    transition_relations.append((THIRD_STATE_NAME, "A", FIRST_STATE_NAME, ""))
    transition_relations.append((THIRD_STATE_NAME, "U", FIRST_STATE_NAME, ""))
    transition_relations.append((THIRD_STATE_NAME, "C", FIRST_STATE_NAME, ""))

    # Start kodon - třetí nukleotid.
    transition_relations.append((THIRD_STATE_NAME, "G", FOURTH_STATE_NAME, PROTEIN_START_LABEL + "M"))

    # Stop kodon.
    transition_relations.append((FOURTH_STATE_NAME, "UAA", FIRST_STATE_NAME, PROTEIN_END_LABEL))
    transition_relations.append((FOURTH_STATE_NAME, "UAG", FIRST_STATE_NAME, PROTEIN_END_LABEL))
    transition_relations.append((FOURTH_STATE_NAME, "UGA", FIRST_STATE_NAME, PROTEIN_END_LABEL))

    # Konverze.

    # Ala.
    transition_relations.append((FOURTH_STATE_NAME, "GCA", FOURTH_STATE_NAME, "A"))
    transition_relations.append((FOURTH_STATE_NAME, "GCC", FOURTH_STATE_NAME, "A"))
    transition_relations.append((FOURTH_STATE_NAME, "GCG", FOURTH_STATE_NAME, "A"))
    transition_relations.append((FOURTH_STATE_NAME, "GCU", FOURTH_STATE_NAME, "A"))

    # Arg.
    transition_relations.append((FOURTH_STATE_NAME, "AGA", FOURTH_STATE_NAME, "R"))
    transition_relations.append((FOURTH_STATE_NAME, "AGG", FOURTH_STATE_NAME, "R"))
    transition_relations.append((FOURTH_STATE_NAME, "CGA", FOURTH_STATE_NAME, "R"))
    transition_relations.append((FOURTH_STATE_NAME, "CGC", FOURTH_STATE_NAME, "R"))
    transition_relations.append((FOURTH_STATE_NAME, "CGG", FOURTH_STATE_NAME, "R"))
    transition_relations.append((FOURTH_STATE_NAME, "CGU", FOURTH_STATE_NAME, "R"))

    # Asp.
    transition_relations.append((FOURTH_STATE_NAME, "GAC", FOURTH_STATE_NAME, "D"))
    transition_relations.append((FOURTH_STATE_NAME, "GAU", FOURTH_STATE_NAME, "D"))

    # Asn.
    transition_relations.append((FOURTH_STATE_NAME, "AAC", FOURTH_STATE_NAME, "N"))
    transition_relations.append((FOURTH_STATE_NAME, "AAU", FOURTH_STATE_NAME, "N"))

    # Cys.
    transition_relations.append((FOURTH_STATE_NAME, "UGC", FOURTH_STATE_NAME, "C"))
    transition_relations.append((FOURTH_STATE_NAME, "UGU", FOURTH_STATE_NAME, "C"))

    # Glu.
    transition_relations.append((FOURTH_STATE_NAME, "GAA", FOURTH_STATE_NAME, "E"))
    transition_relations.append((FOURTH_STATE_NAME, "GAG", FOURTH_STATE_NAME, "E"))

    # Gln.
    transition_relations.append((FOURTH_STATE_NAME, "CAA", FOURTH_STATE_NAME, "Q"))
    transition_relations.append((FOURTH_STATE_NAME, "CAG", FOURTH_STATE_NAME, "Q"))

    # Gly.
    transition_relations.append((FOURTH_STATE_NAME, "GGA", FOURTH_STATE_NAME, "G"))
    transition_relations.append((FOURTH_STATE_NAME, "GGC", FOURTH_STATE_NAME, "G"))
    transition_relations.append((FOURTH_STATE_NAME, "GGG", FOURTH_STATE_NAME, "G"))
    transition_relations.append((FOURTH_STATE_NAME, "GGU", FOURTH_STATE_NAME, "G"))

    # His.
    transition_relations.append((FOURTH_STATE_NAME, "CAC", FOURTH_STATE_NAME, "H"))
    transition_relations.append((FOURTH_STATE_NAME, "CAU", FOURTH_STATE_NAME, "H"))

    # Ile.
    transition_relations.append((FOURTH_STATE_NAME, "AUA", FOURTH_STATE_NAME, "I"))
    transition_relations.append((FOURTH_STATE_NAME, "AUC", FOURTH_STATE_NAME, "I"))
    transition_relations.append((FOURTH_STATE_NAME, "AUU", FOURTH_STATE_NAME, "I"))

    # Leu.
    transition_relations.append((FOURTH_STATE_NAME, "UUA", FOURTH_STATE_NAME, "L"))
    transition_relations.append((FOURTH_STATE_NAME, "UUG", FOURTH_STATE_NAME, "L"))
    transition_relations.append((FOURTH_STATE_NAME, "CUA", FOURTH_STATE_NAME, "L"))
    transition_relations.append((FOURTH_STATE_NAME, "CUC", FOURTH_STATE_NAME, "L"))
    transition_relations.append((FOURTH_STATE_NAME, "CUG", FOURTH_STATE_NAME, "L"))
    transition_relations.append((FOURTH_STATE_NAME, "CUU", FOURTH_STATE_NAME, "L"))

    # Lys.
    transition_relations.append((FOURTH_STATE_NAME, "AAA", FOURTH_STATE_NAME, "K"))
    transition_relations.append((FOURTH_STATE_NAME, "AAG", FOURTH_STATE_NAME, "K"))

    # Met.
    transition_relations.append((FOURTH_STATE_NAME, "AUG", FOURTH_STATE_NAME, "M"))

    # Phe.
    transition_relations.append((FOURTH_STATE_NAME, "UUC", FOURTH_STATE_NAME, "F"))
    transition_relations.append((FOURTH_STATE_NAME, "UUU", FOURTH_STATE_NAME, "F"))

    # Pro.
    transition_relations.append((FOURTH_STATE_NAME, "CCA", FOURTH_STATE_NAME, "P"))
    transition_relations.append((FOURTH_STATE_NAME, "CCC", FOURTH_STATE_NAME, "P"))
    transition_relations.append((FOURTH_STATE_NAME, "CCG", FOURTH_STATE_NAME, "P"))
    transition_relations.append((FOURTH_STATE_NAME, "CCU", FOURTH_STATE_NAME, "P"))

    # Ser.
    transition_relations.append((FOURTH_STATE_NAME, "AGC", FOURTH_STATE_NAME, "S"))
    transition_relations.append((FOURTH_STATE_NAME, "AGU", FOURTH_STATE_NAME, "S"))
    transition_relations.append((FOURTH_STATE_NAME, "UCA", FOURTH_STATE_NAME, "S"))
    transition_relations.append((FOURTH_STATE_NAME, "UCC", FOURTH_STATE_NAME, "S"))
    transition_relations.append((FOURTH_STATE_NAME, "UCG", FOURTH_STATE_NAME, "S"))
    transition_relations.append((FOURTH_STATE_NAME, "UCU", FOURTH_STATE_NAME, "S"))

    # Thr.
    transition_relations.append((FOURTH_STATE_NAME, "ACA", FOURTH_STATE_NAME, "T"))
    transition_relations.append((FOURTH_STATE_NAME, "ACC", FOURTH_STATE_NAME, "T"))
    transition_relations.append((FOURTH_STATE_NAME, "ACG", FOURTH_STATE_NAME, "T"))
    transition_relations.append((FOURTH_STATE_NAME, "ACU", FOURTH_STATE_NAME, "T"))

    # Trp.
    transition_relations.append((FOURTH_STATE_NAME, "UGG", FOURTH_STATE_NAME, "W"))

    # Tyr.
    transition_relations.append((FOURTH_STATE_NAME, "UAC", FOURTH_STATE_NAME, "Y"))
    transition_relations.append((FOURTH_STATE_NAME, "UAU", FOURTH_STATE_NAME, "Y"))

    # Val.
    transition_relations.append((FOURTH_STATE_NAME, "GUA", FOURTH_STATE_NAME, "V"))
    transition_relations.append((FOURTH_STATE_NAME, "GUC", FOURTH_STATE_NAME, "V"))
    transition_relations.append((FOURTH_STATE_NAME, "GUG", FOURTH_STATE_NAME, "V"))
    transition_relations.append((FOURTH_STATE_NAME, "GUU", FOURTH_STATE_NAME, "V"))

    initial_state = FIRST_STATE_NAME

    if non_terminated:
        final_states = {FIRST_STATE_NAME, SECOND_STATE_NAME, THIRD_STATE_NAME, FOURTH_STATE_NAME}
    else:
        final_states = {FIRST_STATE_NAME, SECOND_STATE_NAME, THIRD_STATE_NAME}

    return FiniteTransducer(transition_relations, initial_state, final_states)
