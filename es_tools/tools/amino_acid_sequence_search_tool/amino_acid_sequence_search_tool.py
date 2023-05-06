"""Nástroj pro vyhledávání proteinů a sekvencí aminokyselin proteinů.

Projekt: Bakalářská práce Regulované jazykové operace a jejich užití, Brno 2023.

Tento soubor obsahuje třídu nástroje reprezentujícího aplikaci vymazávacího systému pro vyhledávání proteinů a sekvencí
aminokyselin proteinů.

:Author: David Chocholatý
:Contact: xchoch09@stud.fit.vutbr.cz
:Filename: amino_acid_sequence_search_tool.py
"""

import argparse
import sys

from es_tools.custom_exceptions.final_states_not_states_subset_exception import FinalStatesNotStatesSubsetException
from es_tools.custom_exceptions.illegal_symbol_occurrence_exception import IllegalSymbolOccurrenceException
from es_tools.custom_exceptions.initial_state_not_in_states_exception import InitialStateNotInStatesException
from es_tools.custom_exceptions.internal_error_exception import InternalErrorException
from es_tools.custom_exceptions.invalid_argument_exception import InvalidArgumentException
from es_tools.custom_exceptions.invalid_input_data_structure_exception import InvalidInputDataStructure
from es_tools.custom_exceptions.invalid_regular_language_pattern_exception import InvalidRegularLanguagePatternException
from es_tools.custom_exceptions.invalid_searched_sequences_exception import InvalidSearchedSequencesException
from es_tools.custom_exceptions.maximum_input_string_length_exceeded_exception import \
    MaximumInputStringLengthExceededException
from es_tools.custom_exceptions.required_argument_not_provided_exception import RequiredArgumentNotProvidedException
from es_tools.error_utils.exit_code import ExitCode
from es_tools.handlers.argument_handler.argument_handler import ArgumentHandler
from es_tools.tools.amino_acid_sequence_search_tool.custom_utils.custom_constants \
    import INPUT_LINES_NUMBER
from es_tools.shared_utils.shared_constants import SUBSEQUENCE_LABEL
from es_tools.tools.amino_acid_sequence_search_tool.custom_utils.custom_transducer_creation \
    import create_transducer_triplets_processing
from es_tools.shared_utils.transducer_creation_sequences_labelling import create_transducer_subsequences_labelling
from es_tools.tools.amino_acid_sequence_search_tool.custom_utils.possible_symbols import possible_symbols
from es_tools.tools.amino_acid_sequence_search_tool.custom_utils.custom_erasing_system_creation \
    import create_custom_erasing_system
from es_tools.tools.amino_acid_sequence_search_tool.custom_utils.valid_searched_sequences import \
    valid_searched_sequences
from es_tools.tools.amino_acid_sequence_search_tool.custom_utils.custom_constants import PROTEIN_START_LABEL,\
    PROTEIN_END_LABEL
from es_tools.tools.tool import Tool


class AminoAcidSequenceSearchTool(Tool):
    """Nástroj reprezentující aplikaci pro vyhledávání proteinů a sekvencí aminokyselin proteinů.

    Tato třída implementuje nástroj realizující navržený algoritmus aplikující vymazávací systém na vyhledávání
    proteinů a sekvencí aminokyselin proteinů pro RNA sekvenci. Hlavní algoritmus představený v textu práce na stranách
    54-57 reprezentuje metoda _run_main_algorithm().
    """
    def __init__(self) -> None:
        """**Konstruktor třídy AminoAcidSequenceSearchTool**

        Konstruktor slouží pouze pro nastavení základních hodnot atributů třídy, přičemž jsou nastaveny atributy
        zdědené od rodičovské třídy Tool. Třemi atributy, které jsou specifické pro třídu
        AminoAcidSequenceSearchTool, jsou atributy __subsequences, __sequences a __non_terminated. Atribut
        __subsequences určuje vyhledávané podsekvence aminokyselin proteinů, atribut __sequences sekvence aminokyselin
        kódující příslušný protein a atribut __non_terminated určuje, zda může RNA sekvence končit i proteinem, který
        není ukončen takzvaným stop kodonem, přičemž je dodržený převod po trojicích nukleotidů.
        """
        super().__init__(INPUT_LINES_NUMBER)
        self.__subsequences = list()
        self.__sequences = list()
        self.__non_terminated = False

    def _add_custom_arguments(self, argument_parser: argparse.ArgumentParser) -> None:
        """Metoda pro přidání specifických uživatelských argumentů pro nástroj.

        Tato metoda implementuje přidání specifických uživatelských argumentů ke společným pro všechny nástroje. Metoda
        přepisuje stejnojmennou metodu z rodičovské třídy Tool.

        :param argument_parser: analyzátor uživatelských argumentů.
        :type argument_parser: argparse.ArgumentParser
        """
        argument_parser.add_argument("-i", "--input", dest="input", type=str,
                                     help="the input file with an RNA sequence on a single line")
        argument_parser.add_argument("-b", "--subseq", dest="subsequences", nargs="*", type=str,
                                     help="the searched amino acid subsequences of proteins")
        argument_parser.add_argument("-s", "--seq", dest="sequences", nargs="*", type=str,
                                     help="the searched whole proteins (their amino acid sequences)")
        argument_parser.add_argument("-n", "--nonterminated", dest="non_terminated", action="store_true",
                                     help="if set, it allows a non terminated protein sequence at the end of the RNA "
                                          "(the coding triplets must still be correct, and the end must be a triplet)")

    def _create_custom_argument_handler(self) -> ArgumentHandler:
        """Metoda pro vytvoření manipulátoru s uživatelskými argumenty.

        Tato metoda implementuje vytvoření manipulátoru s uživatelskými argumenty, přičemž ke společným argumentům jsou
        přidány i specifické pro tento nástroj. Metoda přepisuje stejnojmennou metody z rodičovské třídy Tool.

        :return: manipulátor s uživatelskými argumenty.
        :rtype: ArgumentHandler
        """
        argument_handler = ArgumentHandler(self.get_tool_name())
        self._add_custom_arguments(argument_handler.handler())

        return argument_handler

    def _set_sequences(self) -> None:
        """Nastavení vyhledávaných sekvencí aminokyselin kódujících proteiny.

        Tato metoda slouží pro nastavení vyhledávaných sekvencí aminokyselin kódujících proteiny jako atributů třídy.
        Zároveň jsou provedeny kontroly validity vstupních dat. Dle dalšího návrhu algoritmu jsou proteiny označeny
        počátečním a ukončujícím symbolem.
        """
        if self.arguments.sequences is not None:
            if valid_searched_sequences(self.arguments.sequences):
                self.__sequences = [PROTEIN_START_LABEL + sequence + PROTEIN_END_LABEL
                                    for sequence in self.arguments.sequences]
            else:
                raise InvalidSearchedSequencesException

    def _set_subsequences(self) -> None:
        """Nastavení vyhledávaných podsekvencí aminokyselin proteinů.

        Tato metoda slouží pro nastavení vyhledávaných podsekvencí aminokyselin proteinů jako atributů třídy.
        Zároveň jsou provedeny kontroly validity vstupních dat.
        """
        if self.arguments.subsequences is not None:
            if valid_searched_sequences(self.arguments.subsequences):
                self.__subsequences = self.arguments.subsequences.copy()
            else:
                raise InvalidSearchedSequencesException

    def _set_non_terminated(self) -> None:
        """Nastavení povolení neukončeného proteinu.

        Tato funkce slouží pro nastavení povolení proteinu takového, který se nachází na konci sekvence RNA a není
        ukončen takzvaným stop kodonem. Zároveň se uvažuje dodržení kódování proteinu pro trojicích a nesmí být sekvence
        ukončena nekódujícím počtem jednoho nebo dvou nukleotidů.
        """
        if self.arguments.non_terminated:
            self.__non_terminated = True

    def _load_arguments(self) -> None:
        """Načtení uživatelských argumentů.

        Hlavním cílem této metody je vytvoření manipulátoru s uživatelskými argumenty, včetně přidání specifických
        argumentů ke společným pro všechny nástroje. Zároveň tato metoda, pokud je to možné, provede načtení zadaných
        vstupních hodnot.
        """
        try:
            argument_handler = self._create_custom_argument_handler()
            self.arguments = argument_handler.parse_arguments()
        except InvalidArgumentException:
            raise

        if self.arguments.subsequences is None and self.arguments.sequences is None:
            raise RequiredArgumentNotProvidedException

        if self.arguments.greedy_quantifier is None or self.arguments.verbose is None:
            raise InternalErrorException

        try:
            self._set_sequences()
            self._set_subsequences()
            self._set_non_terminated()
        except InvalidSearchedSequencesException:
            raise

    def _initialize_tool(self) -> None:
        """Inicializace nástroje včetně zpracování vstupních dat.

        Tato metoda slouží pro inicializaci nástroje, to znamená pro načtení vstupních dat ze souboru a zpracování
        uživatelských argumentů.

        :raises OSError: chyba při pokusu o načtení vstupních dat ze souboru (soubor neexistuje, jedná se o adresář,
                         ...).
        :raises InternalErrorException: neočekávaný výskyt interní chyby programu.
        :raises InvalidArgumentException: zadání neplatného uživatelského argumentu.
        :raises InvalidInputDataStructure: neplatná struktura vstupních dat.
        :raises RequiredArgumentNotProvidedException: nezadán požadovaný uživatelský argument.
        :raises InvalidSearchedSequencesException: neplatná vyhledávaná sekvence.
        """
        self.print_tool_name()

        try:
            self._load_arguments()
            self.load_input_data()
        except OSError:
            raise
        except InternalErrorException:
            raise
        except InvalidArgumentException:
            raise
        except InvalidInputDataStructure:
            raise
        except RequiredArgumentNotProvidedException:
            raise
        except InvalidSearchedSequencesException:
            raise

    def _run_main_algorithm(self) -> None:
        """Spuštění hlavního algoritmu nástroje.

        Tato metoda implementuje hlavní tok algoritmu nástroje pro vyhledávání proteinů a sekvencí aminokyselin v RNA.

        :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů převodníku.
        :raises FinalStatesNotStatesSubsetException: množina konečných stavů převodníku není podmnožinou množiny všech
                                                     stavů.
        :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci vymazávacího
                                                  systému.
        :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního jazyka vymazávacího
                                                        systému.
        :raises MaximumInputStringLengthExceededException: překročena maximální povolená délka vstupního řetězce pro
                                                           vymazávací systém.
        """
        input_sequence = self.input_data[0]

        print("Input RNA sequence: " + input_sequence + "\n")

        if self.__sequences is not None and len(self.__subsequences) > 0:
            print("Searched subsequences: " + str(self.__subsequences)[1:-1])

        if self.__sequences is not None and len(self.__sequences) > 0:
            print("Searched sequences: " + str([sequence[1:-1] for sequence in self.__sequences])[1:-1])

        try:
            transducer_triplets_processing = create_transducer_triplets_processing(self.__non_terminated)
        except InitialStateNotInStatesException:
            raise
        except FinalStatesNotStatesSubsetException:
            raise

        generated_output_strings = transducer_triplets_processing.run(input_sequence)
        output_strings = list(generated_output_strings)

        if len(output_strings) != 1:
            raise InvalidInputDataStructure

        try:
            transducer_subsequences_labelling = create_transducer_subsequences_labelling(possible_symbols,
                                                                                         self.__subsequences +
                                                                                         self.__sequences)
        except InitialStateNotInStatesException:
            raise
        except FinalStatesNotStatesSubsetException:
            raise

        generated_output_strings = transducer_subsequences_labelling.run(output_strings[0])
        output_strings = list(generated_output_strings)

        output_strings_with_labels_count = {}
        searched_sequences_number = len(self.__subsequences)

        for output_string in output_strings:
            labels_count = output_string.count(SUBSEQUENCE_LABEL)

            if labels_count >= searched_sequences_number:
                output_strings_with_labels_count.update({output_string: labels_count})

        if len(output_strings_with_labels_count) == 0:
            print("------------------------------------------------------------------------------------\n")
            print("### Input RNA sequence does not meet the requirements ###")
            return

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
        output_strings_with_labels_count = {key: value for key, value in
                                            sorted(output_strings_with_labels_count.items(),
                                                   key=lambda item: item[1], reverse=True)}
        # *** Konec převzatého kódu. ***

        try:
            erasing_system = create_custom_erasing_system(self.__sequences,
                                                          self.__subsequences,
                                                          self.arguments.greedy_quantifier,
                                                          self.arguments.verbose)
        except IllegalSymbolOccurrenceException:
            raise
        except InvalidRegularLanguagePatternException:
            raise

        accepted = False

        for output_string in output_strings_with_labels_count.keys():
            try:
                if erasing_system.run(output_string):
                    accepted = True
                    break
            except MaximumInputStringLengthExceededException:
                raise

        if accepted:
            print("------------------------------------------------------------------------------------\n")
            print("### Input RNA sequence meets the requirements ###")
        else:
            print("------------------------------------------------------------------------------------\n")
            print("### Input RNA sequence does not meet the requirements ###")

    def run(self) -> None:
        """Spuštění běhu nástroje.

        Cílem této metody je spuštění inicializace nástroje a poté samotného hlavního algoritmu implementované aplikace
        vymazávacího systému.

        :raises OSError: chyba při pokusu o načtení vstupních dat ze souboru (soubor neexistuje, jedná se o adresář,
                         ...).
        :raises InternalErrorException: neočekávaný výskyt interní chyby programu.
        :raises InvalidArgumentException: zadání neplatného uživatelského argumentu.
        :raises InvalidInputDataStructure: neplatná struktura vstupních dat.
        :raises IllegalSymbolOccurrenceException: výskyt nepovoleného symbolu ve vymazávacím řetězci vymazávacího
                                                  systému.
        :raises InvalidRegularLanguagePatternException: nevalidní nebo nepovolený tvar regulárního jazyka vymazávacího
                                                        systému.
        :raises MaximumInputStringLengthExceededException: překročena maximální povolená délka vstupního řetězce pro
                                                           vymazávací systém.
        :raises InitialStateNotInStatesException: počáteční stav nenáleží do množiny stavů převodníku.
        :raises FinalStatesNotStatesSubsetException: množina konečných stavů převodníku není podmnožinou množiny všech
                                                     stavů.
        :raises RequiredArgumentNotProvidedException: nezadán požadovaný uživatelský argument.
        :raises InvalidSearchedSequencesException: neplatná vyhledávaná sekvence.
        """
        try:
            self._initialize_tool()
        except OSError:
            raise
        except InternalErrorException:
            raise
        except InvalidArgumentException:
            raise
        except InvalidInputDataStructure:
            raise
        except RequiredArgumentNotProvidedException:
            raise
        except InvalidSearchedSequencesException:
            raise

        try:
            self._run_main_algorithm()
        except InvalidInputDataStructure:
            raise
        except IllegalSymbolOccurrenceException:
            raise
        except InvalidRegularLanguagePatternException:
            raise
        except MaximumInputStringLengthExceededException:
            raise
        except InitialStateNotInStatesException:
            raise
        except FinalStatesNotStatesSubsetException:
            raise


def main() -> None:
    """Hlavní funkce pro spuštění nástroje reprezentujícího aplikaci vymazávacího pro vyhledávání proteinů a sekvencí
    aminokyselin proteinů v RNA."""
    tool = AminoAcidSequenceSearchTool()

    try:
        tool.run()
    except OSError:
        print("\nError: An attempt to open the file failed (an invalid file was provided).")
        sys.exit(ExitCode.FILE_NOT_FOUND.value)
    except InternalErrorException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INTERNAL_ERROR.value)
    except InvalidArgumentException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.WRONG_ARGUMENT.value)
    except InvalidInputDataStructure as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_INPUT_DATA_STRUCTURE.value)
    except RequiredArgumentNotProvidedException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.REQUIRED_ARGUMENT_NOT_PROVIDED.value)
    except InvalidSearchedSequencesException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_ARGUMENT_VALUE.value)
    except IllegalSymbolOccurrenceException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_ERASING_STRING.value)
    except InvalidRegularLanguagePatternException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INVALID_REGULAR_LANGUAGE.value)
    except MaximumInputStringLengthExceededException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.MAXIMUM_INPUT_STRING_LENGTH_EXCEEDED.value)
    except InitialStateNotInStatesException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.INITIAL_STATE_NOT_IN_STATES.value)
    except FinalStatesNotStatesSubsetException as error:
        print("\nError: " + error.msg)
        sys.exit(ExitCode.FINAL_STATES_NOT_STATES_SUBSET.value)


if __name__ == "__main__":
    main()
