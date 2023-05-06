"""Implementace deterministického zobecněného sekvenčního stroje.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje implementaci deterministického zobecněného sekvenčního stroje dle definic uvedených v textu
bakalářské práce na stranách 19-21. Samotnou funkcionalitu implementují metody příslušné třídy
DeterministicGeneralizedSequentialMachine, přičemž hlavní logiku převodníku implementuje metoda run().

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: deterministic_gsm.py
"""

from typing import Generator, List, Set, Tuple

from es_tools.custom_exceptions.final_states_not_states_subset_exception import FinalStatesNotStatesSubsetException
from es_tools.custom_exceptions.initial_state_not_in_states_exception import InitialStateNotInStatesException
from es_tools.custom_exceptions.invalid_transition_exception import InvalidTransitionException
from es_tools.formal_models.transducers.finite_transducer import FiniteTransducer


def generalized_sequential_machine_transitions(transition_relations: List[Tuple[str, str, str, str]]) -> bool:
    """Kontrola, zda přechody uvažují čtení pouze jednotlivých symbolů (je přečten právě jeden symbol ze vstupní pásky).

    :param transition_relations: přechody deterministického zobecněného sekvenčního stroje.
    :type transition_relations: List[Tuple[str, str, str, str]]
    :return: True, pokud přechody splňují podmínku, že je přečten právě jeden symbol ze vstupní pásky.
             V opačném případě False.
    :rtype: bool
    """
    for from_state, input_string, to_state, output_string in transition_relations:
        if len(input_string) != 1:
            return False

    return True


def check_determinism(transition_relations: List[Tuple[str, str, str, str]]) -> None:
    """Kontrola, zda přechody splňují podmínky deterministického zobecněného sekvenčního stroje.

    Tato funkce provádí kontrolu podmínek pro přechody deterministického zobecněného sekvenčního stroje. S využitím
    funkce generalized_sequential_machine_transitions() se kontroluje, zda platí podmínky pro zobecněný
    sekvenční stroj, tedy zda jsou ze vstupní pásky čteny pouze symboly. Samotná funkce poté provádí kontrolu
    determinismu přechodů.

    :param transition_relations: přechody deterministického zobecněného sekvenčního stroje.
    :type transition_relations: List[Tuple[str, str, str, str]]
    :raises InvalidTransitionException: přechody nesplňují podmínky deterministického zobecněného sekvenčního stroje.
    """
    if not generalized_sequential_machine_transitions(transition_relations):
        raise InvalidTransitionException

    seen_input_symbols = set()

    # Kontrola samotného determinismu přechodů.
    for from_state, input_symbol, to_state, output_string in transition_relations:
        if (from_state, input_symbol) in seen_input_symbols:
            raise InvalidTransitionException

        seen_input_symbols.add((from_state, input_symbol))


class DeterministicGeneralizedSequentialMachine(FiniteTransducer):
    """Implementace deterministického zobecněného sekvenčního stroje

    Tato třída poskytuje metody, které implementují funkcionalitu deterministického zobecněného sekvenčního stroje.
    Základ této třídy vychází ze třídy FiniteTransducer implementující konečný převodník. Kromě konstruktoru třída
    obsahuje implementaci metody run(), která provádí zpracování vstupního řetězce a generování výstupních řetězců
    s využitím deterministického zobecněného sekvenčního stroje.
    """
    def __init__(self, transition_relations: List[Tuple[str, str, str, str]], initial_state: str,
                 final_states: Set[str]) -> None:
        """**Konstruktor třídy DeterministicGeneralizedSequentialMachine**

        Konstruktor slouží především pro nastavení základních entit deterministického zobecněného sekvenčního stroje,
        a to včetně elementů společných s konečným převodníkem (FiniteTransducer). Zároveň probíhá kontrola, zda
        přechody stroje splňují požadované podmínky, a to determinismus přechodů a čtení pouze jednotlivých symbolů
        ze vstupní pásky.

        :param transition_relations: přechody deterministického zobecněného sekvenčního stroje.
        :type transition_relations: List[Tuple[str, str, str, str]]
        :param initial_state: počáteční stav.
        :type initial_state: str
        :param final_states: množina koncových stavů.
        :type final_states: Set[str]
        :raises InvalidTransitionException: neplatný přechod deterministického zobecněného sekvenčního stroje.
        :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů.
        :raises FinalStatesNotStatesSubsetException: množina koncových stavů není podmnožinou množiny stavů.
        """
        try:
            check_determinism(transition_relations)
            super().__init__(transition_relations, initial_state, final_states)
        except InvalidTransitionException:
            raise
        except InitialStateNotInStatesException:
            raise
        except FinalStatesNotStatesSubsetException:
            raise

    def run(self, input_string: str) -> Generator[str, None, None]:
        """Spuštění běhu definovaného deterministického zobecněného sekvenčního stroje.

        Tato metoda poskytuje fundamentální funkcionalitu běhu deterministického zobecněného sekvenčního stroje.
        Zároveň metoda přepisuje stejnojmennou metodu rodičovské třídy FiniteTransducer.

        :param input_string: vstupní řetězec.
        :type input_string: str
        :return: navrací vygenerovaný výstupní řetězec (pouze jeden).
        :rtype: Generator[str, None, None]
        """
        current_state = self.initial_state_
        output_string = ""

        while input_string != "":
            # Přečtení symbolu ze vstupní pásky.
            input_symbol = input_string[0]

            next_transition = self.transition_relations_.get((current_state, input_symbol))

            if next_transition is None:
                return

            next_state, transition_output_string = next_transition[0]

            current_state = next_state
            output_string = output_string + transition_output_string

            # Posunutí čtecí hlavy o jeden symbol.
            input_string = input_string[1:]

        # Pokud po přečtení celého vstupního řetězce stav, ve kterém se aktuální deterministický zobecněný sekvenční
        # stroj nachází, náleží do množiny koncových stavů, poté je navrácen výstupní řetězec.
        if current_state in self.final_states_:
            yield output_string
