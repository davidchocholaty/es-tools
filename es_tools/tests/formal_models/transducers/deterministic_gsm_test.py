"""Testy pro deterministický zobecněný sekvenční stroj.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje testy pro ověření správnosti implementace deterministického zobecněného sekvenčního stroje.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: deterministic_gsm_test.py
"""

import unittest

from es_tools.custom_exceptions.final_states_not_states_subset_exception import FinalStatesNotStatesSubsetException
from es_tools.custom_exceptions.initial_state_not_in_states_exception import InitialStateNotInStatesException
from es_tools.custom_exceptions.invalid_transition_exception import InvalidTransitionException
from es_tools.formal_models.transducers.deterministic_gsm import DeterministicGeneralizedSequentialMachine


class DeterministicGeneralizedSequentialMachineTest(unittest.TestCase):
    """Třída obsahující jednotkové testy pro deterministický zobecněný sekvenční stroj.

    Tato třída obsahuje jednotkové testy pro ověření správnosti implementace deterministického zobecněného
    sekvenčního stroje.
    """

    def test_initial_state_not_in_states(self) -> None:
        """Testování případu, kdy počáteční stav nenáleží do množiny stavů deterministického zobecněného sekvenčního
        stroje."""
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "b", "s", "")]
        initial_state = "t"
        final_states = {"s"}

        with self.assertRaises(InitialStateNotInStatesException):
            DeterministicGeneralizedSequentialMachine(transition_relations, initial_state, final_states)

    def test_final_states_not_states_subset(self) -> None:
        """Testování případu, kdy množina koncových stavů není podmnožinou množiny koncových stavů."""
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "b", "s", "")]
        initial_state = "s"
        final_states = {"s", "t"}

        with self.assertRaises(FinalStatesNotStatesSubsetException):
            DeterministicGeneralizedSequentialMachine(transition_relations, initial_state, final_states)

    def test_invalid_transition_gsm(self) -> None:
        """Testování případu, kdy přechody nesplňují požadavky pro zobecněný sekvenční stroj."""
        # S prázdným řetězcem na vstupu.
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "", "s", "")]
        initial_state = "s"
        final_states = {"s"}

        with self.assertRaises(InvalidTransitionException):
            DeterministicGeneralizedSequentialMachine(transition_relations, initial_state, final_states)

        #  S řetězcem na vstupu, který obsahuje dva a více symbolů.
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "bd", "s", "")]

        with self.assertRaises(InvalidTransitionException):
            DeterministicGeneralizedSequentialMachine(transition_relations, initial_state, final_states)

    def test_invalid_transition_determinism(self) -> None:
        """Testování případu, kdy přechody nesplňují požadavky pro deterministický zobecněný sekvenční stroj."""
        transition_relations = [("s", "a", "r", "c"),
                                ("s", "a", "t", "d"),
                                ("r", "b", "s", "e"),
                                ("t", "b", "s", "f")]
        initial_state = "s"
        final_states = {"s"}

        with self.assertRaises(InvalidTransitionException):
            DeterministicGeneralizedSequentialMachine(transition_relations, initial_state, final_states)

    def test_accept_empty_string(self) -> None:
        """Testování přijetí také prázdného řetězce (epsilon) deterministickým zobecněným sekvenčním strojem
        a vygenerování výstupu."""
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "b", "s", "")]
        initial_state = "s"
        final_states = {"s"}

        transducer = DeterministicGeneralizedSequentialMachine(transition_relations, initial_state, final_states)

        generated_output_strings = transducer.run("")
        output_strings = list(generated_output_strings)

        self.assertEqual(len(output_strings), 1)
        self.assertEqual(output_strings[0], "")

    def test_valid_string_acceptance(self) -> None:
        """Testování správného přijetí vstupního řetězce deterministickým zobecněným sekvenčním strojem
        a vygenerování výstupu."""
        transition_relations = [("s", "a", "r", "cd"),
                                ("r", "b", "s", "")]
        initial_state = "s"
        final_states = {"s"}

        transducer = DeterministicGeneralizedSequentialMachine(transition_relations, initial_state, final_states)

        generated_output_strings = transducer.run("abab")
        output_strings = list(generated_output_strings)

        self.assertEqual(len(output_strings), 1)
        self.assertEqual(output_strings[0], "cdcd")

    def test_valid_string_rejection(self) -> None:
        """Testování správného odmítnutí vstupního řetězce deterministickým zobecněným sekvenčním strojem."""
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "b", "s", "d")]
        initial_state = "s"
        final_states = {"s"}

        transducer = DeterministicGeneralizedSequentialMachine(transition_relations, initial_state, final_states)

        generated_output_string = transducer.run("ababa")
        output_strings = list(generated_output_string)

        self.assertEqual(len(output_strings), 0)


if __name__ == "__main__":
    unittest.main()
