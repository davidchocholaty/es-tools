"""Testy pro konečný převodník.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje testy pro ověření správnosti implementace konečného převodníku.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: finite_transducer_test.py
"""

import unittest

from es_tools.custom_exceptions.final_states_not_states_subset_exception import FinalStatesNotStatesSubsetException
from es_tools.custom_exceptions.initial_state_not_in_states_exception import InitialStateNotInStatesException
from es_tools.formal_models.transducers.finite_transducer import FiniteTransducer


class FiniteTransducerTest(unittest.TestCase):
    """Třída obsahující jednotkové testy pro konečný převodník.

    Tato třída obsahuje jednotkové testy pro ověření správnosti implementace konečného převodníku.
    """

    def test_initial_state_not_in_states(self) -> None:
        """Testování případu, kdy počáteční stav nenáleží do množiny stavů konečného převodníku."""
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "b", "s", "")]
        initial_state = "t"
        final_states = {"s"}

        with self.assertRaises(InitialStateNotInStatesException):
            FiniteTransducer(transition_relations, initial_state, final_states)

    def test_final_states_not_states_subset(self) -> None:
        """Testování případu, kdy množina koncových stavů není podmnožinou množiny koncových stavů."""
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "b", "s", "")]
        initial_state = "s"
        final_states = {"s", "t"}

        with self.assertRaises(FinalStatesNotStatesSubsetException):
            FiniteTransducer(transition_relations, initial_state, final_states)

    def test_accept_empty_string(self) -> None:
        """Testování přijetí také prázdného řetězce (epsilon) konečným převodníkem a vygenerování výstupu."""
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "b", "s", "")]
        initial_state = "s"
        final_states = {"s"}

        transducer = FiniteTransducer(transition_relations, initial_state, final_states)

        generated_output_strings = transducer.run("")
        output_strings = list(generated_output_strings)

        self.assertEqual(len(output_strings), 1)
        self.assertEqual(output_strings[0], "")

    def test_valid_string_acceptance(self) -> None:
        """Testování správného přijetí vstupního řetězce konečným převodníkem a vygenerování výstupu."""
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "b", "s", "")]
        initial_state = "s"
        final_states = {"s"}

        transducer = FiniteTransducer(transition_relations, initial_state, final_states)

        generated_output_strings = transducer.run("abab")
        output_strings = list(generated_output_strings)

        self.assertEqual(len(output_strings), 1)
        self.assertEqual(output_strings[0], "cc")

        # S řetězcem na vstupní straně přechodu.
        transition_relations = [("s", "ab", "r", "cd"),
                                ("r", "ef", "s", "")]

        second_transducer = FiniteTransducer(transition_relations, initial_state, final_states)

        generated_output_strings = second_transducer.run("abefabef")
        output_strings = list(generated_output_strings)

        self.assertEqual(len(output_strings), 1)
        self.assertEqual(output_strings[0], "cdcd")

    def test_valid_string_rejection(self) -> None:
        """Testování správného odmítnutí vstupního řetězce konečným převodníkem."""
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "b", "s", "d")]
        initial_state = "s"
        final_states = {"s"}

        transducer = FiniteTransducer(transition_relations, initial_state, final_states)

        generated_output_string = transducer.run("ababa")
        output_strings = list(generated_output_string)

        self.assertEqual(len(output_strings), 0)

        # S řetězcem na vstupní straně přechodu.
        transition_relations = [("s", "ab", "r", "cd"),
                                ("r", "ef", "s", "")]

        second_transducer = FiniteTransducer(transition_relations, initial_state, final_states)

        generated_output_strings = second_transducer.run("abefab")
        output_strings = list(generated_output_strings)

        self.assertEqual(len(output_strings), 0)

    # The transition with an empty input string is the last one used.
    def test_empty_string_transition_as_last(self) -> None:
        """Testování případu, kdy při posledním použitém přechodu je přečten prázdný symbol (epsilon)."""
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "", "s", "")]
        initial_state = "s"
        final_states = {"s"}

        transducer = FiniteTransducer(transition_relations, initial_state, final_states)

        generated_output_strings = transducer.run("aaaa")
        output_strings = list(generated_output_strings)

        self.assertEqual(len(output_strings), 1)
        self.assertEqual(output_strings[0], "cccc")

    def test_exceeding_maximum_output_string_length_no_empty_string(self) -> None:
        """Testování překročení maximální povolené délky výstupního řetězce pro případ, kdy převodník neobsahuje
        přechod s prázdným řetězcem na vstupní straně."""
        transition_relations = [("s", "a", "r", "c"),
                                ("r", "b", "s", "d")]
        initial_state = "s"
        final_states = {"s"}

        max_output_string_length_level = 2
        transducer = FiniteTransducer(transition_relations, initial_state, final_states, max_output_string_length_level)

        generated_output_string = transducer.run("ab")
        output_strings = list(generated_output_string)

        self.assertEqual(len(output_strings), 1)
        self.assertEqual(output_strings[0], "cd")

        generated_output_string = transducer.run("abab")
        output_strings = list(generated_output_string)

        self.assertEqual(len(output_strings), 1)
        self.assertEqual(output_strings[0], "cdcd")

    def test_exceeding_maximum_output_string_length_with_empty_string(self) -> None:
        """Testování překročení maximální povolené délky výstupního řetězce pro případ, kdy převodník obsahuje
        přechod s prázdným řetězcem na vstupní straně."""
        max_output_string_length_level = 20
        expected_output_strings = ["abefg",
                                   "abcdabefg",
                                   "abcdabcdabefg",
                                   "abcdabcdabcdabefg",
                                   "abcdabcdabcdabcdabefg"]

        transition_relations = [("s", "", "r", "ab"),
                                ("r", "", "s", "cd"),
                                ("r", "aa", "f", "efg")]
        initial_state = "s"
        final_states = {"f"}

        transducer = FiniteTransducer(transition_relations, initial_state, final_states, max_output_string_length_level)

        generated_output_string = transducer.run("aa")
        output_strings = list(generated_output_string)

        self.assertCountEqual(output_strings, expected_output_strings)
        self.assertListEqual(output_strings, expected_output_strings)

    def test_non_deterministic_finite_transducer(self) -> None:
        """Testování nedeterministického konečného převodníku."""
        expected_output_strings = ["efefefef",
                                   "efefabcd",
                                   "efabcdef",
                                   "abcdefef",
                                   "abcdabcd"]

        transition_relations = [("s", "a", "r", "ab"),
                                ("r", "a", "s", "cd"),
                                ("s", "a", "s", "ef")]
        initial_state = "s"
        final_states = {"s"}

        transducer = FiniteTransducer(transition_relations, initial_state, final_states)

        generated_output_string = transducer.run("aaaa")
        output_strings = list(generated_output_string)

        self.assertCountEqual(output_strings, expected_output_strings)
        self.assertListEqual(output_strings, expected_output_strings)


if __name__ == "__main__":
    unittest.main()
